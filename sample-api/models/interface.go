package models

import "time"

// ApplicationInfo represents basic application details
type ApplicationInfo struct {
	Name        string    `json:"name"`
	Version     string    `json:"version"`
	Environment string    `json:"environment"`
	StartTime   time.Time `json:"start_time"`
}

// SystemMetrics represents system metrics
type SystemMetrics struct {
	Timestamp       time.Time `json:"timestamp"`
	Uptime          string    `json:"uptime"`
	NumCPU          int       `json:"num_cpu"`
	GoVersion       string    `json:"go_version"`
	MemoryTotal     uint64    `json:"memory_total_mb"`
	MemoryAvailable uint64    `json:"memory_available_mb"`
	CPUUsage        float64   `json:"cpu_usage_percent"`
	DiskUsage       float64   `json:"disk_usage_percent"`
}

type HealthStatus struct {
	Status  string `json:"status"`
	Message string `json:"message"`
}
