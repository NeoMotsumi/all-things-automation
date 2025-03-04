package handlers

import (
	"log"
	"net/http"
	"runtime"
	"time"

	"github.com/NeoMotsumi/all-things-automation/models"
	"github.com/gin-gonic/gin"
	"github.com/shirou/gopsutil/cpu"
	"github.com/shirou/gopsutil/disk"
	"github.com/shirou/gopsutil/mem"
)

var (
	appInfo = models.ApplicationInfo{
		Name:        "All Things Automation",
		Version:     "1.0.0",
		Environment: "dev",
		StartTime:   time.Now(),
	}
)

// can be used as initializer
type DiagnosticsHandler struct {
}

func NewDiagnosticsHandler() *DiagnosticsHandler {
	return &DiagnosticsHandler{}
}

func (h *DiagnosticsHandler) GetDiagnostics(c *gin.Context) {
	diagnostics := struct {
		Application models.ApplicationInfo `json:"application"`
		System      *models.SystemMetrics  `json:"system"`
	}{
		Application: appInfo,
		System:      getSystemMetrics(),
	}
	c.JSON(http.StatusOK, diagnostics)
}

func getSystemMetrics() *models.SystemMetrics {
	virtualMemory, err := mem.VirtualMemory()
	if err != nil {
		log.Println("Error getting memory metrics:", err)
	}

	cpuUsage, err := cpu.Percent(time.Second, false)
	if err != nil {
		log.Println("Error getting CPU usage:", err)
	}

	diskStat, err := disk.Usage("/")
	if err != nil {
		log.Println("Error getting disk usage:", err)
	}

	return &models.SystemMetrics{
		Timestamp:       time.Now(),
		Uptime:          time.Since(appInfo.StartTime).String(),
		NumCPU:          runtime.NumCPU(),
		GoVersion:       runtime.Version(),
		MemoryTotal:     virtualMemory.Total / 1024 / 1024,
		MemoryAvailable: virtualMemory.Available / 1024 / 1024,
		CPUUsage:        cpuUsage[0],
		DiskUsage:       diskStat.UsedPercent,
	}
}
