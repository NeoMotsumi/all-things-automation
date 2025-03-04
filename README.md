# All Things Automation

**Note:** This repository is solely meant for educational purposes.

## Overview

This repository demonstrates various automation techniques for modern cloud-native applications, including:

* Setting up a local Kubernetes test cluster
* Implementing GitOps with ArgoCD for continuous deployment
* Creating and instrumenting a sample application with Prometheus metrics
* Visualizing application performance with Grafana dashboards
* Implementing high availability (HA) architecture patterns

## Project Structure

| Directory/File | Description |
|----------------|-------------|
| [sample-api/](./sample-api/) | Golang API application demonstrating the deployment workflow |
| [argocd-apps/](./argocd-apps/) | ArgoCD application definitions (system apps and application deployments) |
| [docs/](./docs/) | Documentation for architecture and security strategies |
| [iac/](./iac/) | Infrastructure as Code resources |
| [diagrams/](./diagrams/) | Architecture and workflow diagrams |
| [Taskfile.yaml](./Taskfile.yaml) | Task definitions for automating project setup and deployment |

## Prerequisites

Before getting started, ensure you have the following tools installed:

* [Task](https://taskfile.dev/installation/) - Task runner for executing automation tasks
* [k3d](https://k3d.io/) - Lightweight Kubernetes distribution for local development
* [kubectl](https://kubernetes.io/docs/tasks/tools/) - Kubernetes command-line tool
* [helm](https://helm.sh/docs/intro/install/) - Kubernetes package manager

**Important Note for Colima Users:** To avoid DNS resolution issues, start Colima with:

```bash
colima start --dns 8.8.8.8 --dns 8.8.4.4
```

## Getting Started

### Quick Setup

To set up the complete environment in one command:

```bash
task setup-env
```

This will:
1. Create a Kubernetes cluster using k3d
2. Install ArgoCD for GitOps deployments
3. Deploy system applications (Loki, Prometheus, Grafana, etc.)
4. Deploy the sample application

### Manual Setup

If you prefer to set up components individually:

1. **Create a Kubernetes cluster:**
   ```bash
   task create-cluster
   ```

2. **Install ArgoCD:**
   ```bash
   task install-argocd
   ```

3. **Create a local container registry (optional):**
   ```bash
   task create-registry
   ```

4. **Deploy system applications:**
   ```bash
   task deploy-system-apps
   ```

5. **Deploy the sample application:**
   ```bash
   task deploy-sample-app
   ```

To see all available tasks:

```bash
task --list
```

## Alternative Deployment Methods

The setup above uses a declarative GitOps approach with ArgoCD. For a script-based deployment alternative, see:
[Running your Application Server using a script](./sample-api/scripting/)

## Documentation

This project includes comprehensive documentation:

* [Cloud Architecture for HA Microservices](./docs/cloud-architecture.md) - Architectural overview for running microservices in a high-availability environment
* [Security Strategy](./docs/security-strategy.md) - Comprehensive security approach for cloud deployments


## License

This project is for educational purposes only.

