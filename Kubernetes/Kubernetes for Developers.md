# Kubernetes for Developers

## What is Kubernetes
Kubernetes is an open-source system for automation deployment, scaling, and management of containerized applications

## Why Kubernetes is useful
Kubernetes is useful for making and managing containers for the following reasons:
* Containerize an app which can be sent to other computers or machines efficently
* Scale every container
* Update containers
* Provide networking
* Customize storage

## Kubernetes features
Kubernetes can make the following: <br>
* Pods
* Deployments
* Services
  * Load Balancers
* Rollouts
* Regenerate infrastructure to replace non-healthy ones  
* Storage Options
* Configuration Maps
* Secrets
* Horizontal Scaling

## Kubernetes Layout
* Master Node
  * Controller Manager
  * Store (etcd)
  * API server
  * Scheduler
* Master Node is responsible for controlling:
  * Nodes (1 or more)
    * Pods (1 or more in the Node)
      * Containers    
  * Cluster - Contains many Nodes

# Kubectl
Commands
```
kubectl version
```

```
kubectl cluster-info
```
DNS

```
kubectl get all
```
Get all the resources

```
kubectl run container-name --image name
```

```
kubectl port-forward *pod *ports
```

```
kubectl expose
```

```
kubectl create *resource
```

```
kubectl apply ....
```

