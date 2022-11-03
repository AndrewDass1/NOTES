# Kubernetes Concepts

A manifest can either be in the YAML of JSON format that defines all the needed infrastructure to deploy an application <br>
<br>
Kubernetes manifests are intended to be used to create and automate infrastructure quickly such as pods, deployments, services, containers and more

## Manifest Example File to make a Pod
```
apiVersion: v1
kind: 
metadata: 
  name: *insert name*
  labels:
    app: *insert name*
spec:
  containers:
    - name: *insert name*
      image: ""
      imagePullPolicy: Always
      ports:
        - containerPort: ""
```
In spec section, can specify more than 1 container <br>
<br>
apiversion can be written as: 
```
apiversion: v1 or apiversion: apps/v1
```
apps is a subgroup that contains infrastructure, where each infrastructure has its own yaml files. For example, a ReplicaSet and StatefulSet both have to be defined, two yaml files are needed to define them separately.


## Deploying a Pod
### Commands
```
kubectl apply -f *name*.yml
```
* -f applies a manifest file
* *name* specifies the name of the yaml file, can be anything

```
kubectl get pods --watch
```
If successful, shows if the application is running, the container is created so the Pod is initialized <br>
"READY" shows how much containers are in the pod

```
kubectl get pods -o wide
```
Shows the name, status, restarts, IP and node for pods
```
kubectl get pod --watch
```
Shows what pods are running

```
kubectl delete -f "nameofyamlfile".yml or kubectl delete -f NAME
```
Delete the pod
