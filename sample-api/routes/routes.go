package routes

import (
	"net/http"
	"time"

	"github.com/NeoMotsumi/all-things-automation/handlers"
	"github.com/gin-gonic/gin"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

func SetupRoutes(r *gin.Engine) {
	api := r.Group("/api/v1")
	diagnosticsHandler := handlers.NewDiagnosticsHandler()

	r.GET("/healthz", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"status":    "healthy",
			"timestamp": time.Now(),
		})
	})

	r.GET("/metrics", gin.WrapH(promhttp.Handler()))

	// Diagnostics Handler Routes
	api.GET("/diagnostics", diagnosticsHandler.GetDiagnostics)
}
