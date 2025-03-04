# ArgoCD Apps

This directory contains the ArgoCD apps for the project.

## Installation

```bash
kustomize build argocd-apps | kubectl apply -f -
```

Since this repository is only for demonstration purposes, we will not use overlays, instead we will use the `kustomize build` command to apply the apps.