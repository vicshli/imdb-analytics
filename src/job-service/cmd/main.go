package main

import (
	"fmt"
	"log"
	"net"
	"os"
	"sync"

	pb "../genproto"
	server "../server"

	"github.com/joho/godotenv"
	"google.golang.org/grpc"
)

var (
	envFpath           = "dev.env"
	portEnvKey         = "PORT"
	extractorAPIEnvKey = "EXTRACTOR_API"
)

func mustHaveEnv(key string) (val string) {
	val, exists := os.LookupEnv(key)
	if !exists {
		log.Fatalf("`%s` should be assigned by an environment variable. Exiting...\n", key)
	}
	return val
}

func makeExtractorClient(API string) (pb.ExtractorServiceClient, *grpc.ClientConn, error) {
	conn, err := grpc.Dial(API, grpc.WithInsecure())
	if err != nil {
		return nil, nil, err
	}
	extractorClient := pb.NewExtractorServiceClient(conn)
	return extractorClient, conn, nil
}

func makeJobServiceServer(port string, ec pb.ExtractorServiceClient) (*grpc.Server, net.Listener, *server.JobServer, error) {
	lis, err := net.Listen("tcp", fmt.Sprintf(":%s", port))
	if err != nil {
		return nil, nil, nil, err
	}
	fmt.Printf("Initiating JobService server, listening at port %s\n", port)

	var pendingJobs []int64
	jobSvr := &server.JobServer{
		JobsMap:         make(map[int64]*pb.Job),
		JobsNameToIDMap: make(map[string]int64),
		PendingJobs:     pendingJobs,
		Mu:              &sync.Mutex{},
		Ec:              ec,
	}

	grpcServer := grpc.NewServer()
	pb.RegisterJobServiceServer(grpcServer, jobSvr)

	return grpcServer, lis, jobSvr, nil
}

func main() {
	if err := godotenv.Load(envFpath); err != nil {
		log.Fatalln("Error loading .env file")
	}
	port := mustHaveEnv(portEnvKey)
	extractorAPI := mustHaveEnv(extractorAPIEnvKey)

	extractorClient, conn, err := makeExtractorClient(extractorAPI)
	if err != nil {
		log.Fatalf("%s\n", err)
	}
	defer conn.Close()

	server, lis, jobSvr, err := makeJobServiceServer(port, extractorClient)
	if err != nil {
		log.Fatalf("%s\n", err)
	}

	var wg sync.WaitGroup
	wg.Add(1)
	go func() {
		go jobSvr.ProcessJobs()
		go jobSvr.ProcessJobs()
		go jobSvr.ProcessJobs()
		go jobSvr.ProcessJobs()
		go jobSvr.ProcessJobs()
		server.Serve(lis)
		wg.Done()
	}()
	wg.Wait()
}
