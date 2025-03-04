#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# install application dependencies
install_dependencies() {
    echo "Installing dependencies"
    go mod tidy
}


# build the application
build_application() {
    echo "Building application"
    local target_os=${1:-$(go env GOOS)} #this will ensure that the build uses the correct target OS
    echo "Building for OS: $target_os"
    CGO_ENABLED=0 GOOS=$target_os go build -a -o bin/sample-api main.go
}

# start the api server on the specified port
run_application() {
    echo "Running sample-api"
    ./bin/sample-api server --port 8001
}


main() {
    echo "Packaging and Running Go API..."
    install_dependencies
    build_application
    run_application
}

main