package main

import (
	"fmt"
	"log"
	"os"

	"github.com/NeoMotsumi/all-things-automation/routes"
	"github.com/gin-gonic/gin"
	"github.com/spf13/cobra"
)

func main() {
	gin.SetMode(gin.DebugMode)
	var port string

	var rootCmd = &cobra.Command{
		Use:   "server",
		Short: "All Things Automation API",
		Long:  `All Things Automation API for displaying app diagnostics and usage metrics`,
		Run: func(cmd *cobra.Command, args []string) {
			gin.SetMode(gin.DebugMode)
			r := gin.Default()
			routes.SetupRoutes(r)

			//Start Server
			log.Printf("Server starting on port %s", port)
			if err := r.Run(":" + port); err != nil {
				log.Fatal("Error starting server:", err)
			}
		},
	}

	// Add port flag with default value
	rootCmd.Flags().StringVarP(&port, "port", "p", "8080", "Port to run the server on")

	if err := rootCmd.Execute(); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}
