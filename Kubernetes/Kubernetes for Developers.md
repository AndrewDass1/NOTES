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
Shows the DNS and cluster information

```
kubectl get all
```
Get all the resources

## Pods
Pod - Are the smallest deployable units of computing that you can create and manage in Kubernetes. Is a group of one or more containers, with shared storage and network resources, and a specification for how to run the containers. <br>
<br>
Pod Details: <br>
* Smallest object in Kubernetes
* Pods have:
  * IP
  * Memory
  * Volumes

### Run a Pod
```
kubectl run *podname* --image=""
```
Can use "kubectl apply -f ...", where "..." is the name of the yaml file and is the yaml file is the blueprints to start a pod up <br>
<br>
```
kubectl get pod or kubectl get pods
```
Receive information about a pod or pods
```
kubectl get all
```
Receive information about pods and other Kubernetes objects

### Expose a Pod Port
```
kubectl port-forward *podname 8080:80
```
External port - 8080 <br>
Internal port - 80 <br>
<br>

### Delete Resources
```
kubectl delete pod *podname
```

```
kubectl delete deployment *deployment name
```

## Updating
```
kubectl create -f *name.yml --save-config
```
or use
```
kubectl apply -f *name.yml
```

## Pod Health
