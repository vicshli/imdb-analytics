package server

import (
	"context"
	"fmt"
	"log"
	"math/rand"
	"sync"
	"time"

	pb "../genproto"

	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

// JobServer handles job-related API calls
type JobServer struct {
	JobsMap     map[int64]*pb.Job
	PendingJobs []int64
	Mu          *sync.Mutex
	Ec          pb.ExtractorServiceClient
}

// CreateJob stores a new Job instance in JobServer, and enqueues the new job to the pendings list
func (s *JobServer) CreateJob(ctx context.Context, req *pb.CreateJobRequest) (*pb.CreateJobResponse, error) {
	jid := rand.Int63()
	jobCreated := &pb.Job{Id: jid, TargetName: req.TargetName, Status: pb.Job_NOT_PROCESSED}
	s.JobsMap[jid] = jobCreated
	s.PendingJobs = append(s.PendingJobs, jid)
	return &pb.CreateJobResponse{Successful: true, Job: jobCreated}, nil
}

// GetJob returns a Job instance if found, or an NotFound error if not found
func (s *JobServer) GetJob(ctx context.Context, req *pb.GetJobRequest) (*pb.Job, error) {
	if job, ok := s.JobsMap[req.Id]; ok {
		return job, nil
	}
	return nil, status.Errorf(codes.NotFound, fmt.Sprintf("Job with ID '%d' not found.", req.Id))
}

// GetJobStatus returns the Status of the queried job, if found, or an NotFound error if not found
func (s *JobServer) GetJobStatus(ctx context.Context, req *pb.GetJobRequest) (*pb.JobStatusQueryResponse, error) {
	if job, ok := s.JobsMap[req.Id]; ok {
		return &pb.JobStatusQueryResponse{
			Status:    job.Status,
			StatusMsg: mapJobStatusToMsg(job.Status),
		}, nil
	}
	return nil, status.Errorf(codes.NotFound, fmt.Sprintf("Job with ID '%d' not found.", req.Id))
}

// DeleteJob deletes a job if found; it returns true if a job is found and deleted, otherwise false
func (s *JobServer) DeleteJob(ctx context.Context, req *pb.DeleteJobRequest) (*pb.DeleteJobResponse, error) {
	_, ok := s.JobsMap[req.Id]
	if ok {
		delete(s.JobsMap, req.Id)
	}
	return &pb.DeleteJobResponse{Successful: ok}, nil
}

// processJobs pops Jobs from the waiting queue, calls ExtractorService to perform job,
// and updates the jobs' status based on whether the extraction ended successfully
func (s *JobServer) processJobs() {
	for {
		if len(s.PendingJobs) < 0 {
			time.Sleep(10 * time.Second)
			continue
		}
		if jid, ok := s.popJob(); ok {
			job := s.JobsMap[jid]
			_, err := s.Ec.InitiateExtraction(context.Background(),
				&pb.ExtractionRequest{ItemName: job.TargetName})
			if err != nil {
				log.Println("Error in getting show", err)
				job.Status = pb.Job_COMPLETED_FAILURE
			}
			job.Status = pb.Job_COMPLETED_SUCCESS
		} else {
			log.Println("Attempted to pop from pending jobs but there is no pending jobs.")
		}
	}
}

func (s *JobServer) popJob() (int64, bool) {
	if len(s.PendingJobs) > 0 {
		s.Mu.Lock()
		defer s.Mu.Unlock()
		ret := s.PendingJobs[0]
		s.PendingJobs = s.PendingJobs[1:]
		return ret, true
	}
	return -1, false
}

func mapJobStatusToMsg(status pb.Job_Status) string {
	statusMsgs := map[pb.Job_Status]string{
		pb.Job_NOT_PROCESSED:     "Not Processed",
		pb.Job_PROCESSING:        "Processing",
		pb.Job_COMPLETED_SUCCESS: "Completed Successfully",
		pb.Job_COMPLETED_FAILURE: "Completion failed",
	}
	if msg, ok := statusMsgs[status]; ok {
		return msg
	}
	return fmt.Sprintf("ERR: Job Status Message not found for status '%d'", status)
}