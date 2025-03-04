# All Things Automation

**Note:** This repository is solely meant for educational purposes.

This repository contains a series of tasks to demostrate various ways to automate tasks such as:

* A test kubernetes cluster
* Installing ArgoCD to deploy a sample application
* Creating a sample application, adding prometheus metrics.
* Visualizing application performance metrics using Grafan
* Provide High Level Overview of setting up an HA environment.

## Prerequisites

* [Task](https://taskfile.dev/installation/)
* [k3d](https://k3d.io/)
* [kubectl](https://kubernetes.io/docs/tasks/tools/)
* [helm](https://helm.sh/docs/intro/install/)


**Important Note** if you are colima you might need to run the following, to avoid DNS resolution issues:

```bash
colima start --dns 8.8.8.8 --dns 8.8.4.4
```

## Running the project

The taskfile used on the root of this repository will be used to setup your environment to do the following:

* Create a kubernetes cluster using k3d
* Install ArgoCD to the cluster
* Install system applications to the cluster(Loki, Prometheus, Grafana, etc)
* Install a sample application to the cluster

You can run the following command to see all the tasks available:

```bash
task --list
```

If you intend to fully setup your environment, you can run the following command:

```bash
task setup-env
```

This will create a kubernetes cluster, install ArgoCD, install system applications and deploy the sample application.

If you want to create a local registry, you can run the following command:

```bash
task create-registry
```

## Application Definitions


## Definitions

This project is split into a series of tasks, some run in order, others can be run independently.

Below is a list of all the application definitions and tasks that can be excuted:

| Application | Description |
|-------------|-------------|
| [sample-api](./sample-api) | This is a Golang API that well be used to demostrate the entire deployment workflow |
| [argocd-apps](./argocd-apps) | A collection of all application deployments using ArgoCD, currently the directory is separated into system-apps and application deployments |


