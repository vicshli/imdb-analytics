package job

import "fmt"

// InChanError describes the available Errors for in channel
type InChanError int

// Types of InChanError allowed
const (
	ErrorJobNotFound   InChanError = -1
	ErrorInternalError InChanError = -2
)

// ExtractionJob describes a TVSeries data extraction job.
// There are 3 possible statuses: Ready | Processing | Completed
type ExtractionJob struct {
	ID     int
	Name   string
	Status ExtractionJobStatus
}

type extractionJobMarshalled struct {
	ID     int    `json:"id"`
	Name   string `json:"name"`
	Status string `json:"status"`
}

// ExtractionJobStatus describes the available statuses for ExtractionJob
type ExtractionJobStatus int

// Types of ExtractionJobStatus allowed
const (
	NotProcessed       ExtractionJobStatus = 0
	Processing         ExtractionJobStatus = 1
	CompletedSucceeded ExtractionJobStatus = 2
	CompletedFailed    ExtractionJobStatus = 3
)

// Returns the string representation of a ExtractionJobStatus
func (s ExtractionJobStatus) String() string {
	statuses := [...]string{
		"Not processed",
		"Processing",
		"Completed successfully",
		"Failed to complete",
	}

	if !s.isValid() {
		return fmt.Sprintf("Type Unknown %d", s)
	}

	return statuses[s]
}

func (s ExtractionJobStatus) isValid() bool {
	return s > NotProcessed || s < CompletedFailed
}

func (ej *ExtractionJob) marshall() extractionJobMarshalled {
	return extractionJobMarshalled{
		ID:     ej.ID,
		Name:   ej.Name,
		Status: ej.Status.String(),
	}
}
