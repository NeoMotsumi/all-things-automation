# Build stage
FROM golang:1.22.2-alpine AS builder

WORKDIR /app

COPY go.mod go.sum* ./

# Download dependencies
RUN go mod tidy

# Copy source code
COPY . .

# Build the application
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix -o api .

# Final stage - using Chainguard's minimal base
FROM cgr.dev/chainguard/static:latest

WORKDIR /

# Copy the binary from builder
COPY --from=builder /app/api /api

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application
ENTRYPOINT ["/api"] 