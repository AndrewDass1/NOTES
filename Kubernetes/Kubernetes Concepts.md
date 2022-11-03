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


## Services
Helps infrastructure communciate with one another <br>
All the infrastructure is connected by ... <br>
<br>
There are two parts to a service: <br>
* Frontend - Name, IP
* Backend - Load Balancing

### Definitions to Know:
* Abstractions
* ClusterIP
  *  CoreDNS
* Endpoints  

## Node Ports
pod.yml (pod is a placeholder name for the file name, can be anything)
```
apiVersion: v1
kind: Pod
metadata:
  name: *name* (name of pod)
  labels:
    app: *web
spec:
  containers:
    - name: web-ctr
      image: image
      ports:
        - containerPort: 8080
```
nodeport.yml
```
apiVersion: v1
kind: Service
metadata:
  name: ps-nodeport
spec:
  type: NodePort
  ports:
  - port: 80
    targetport: 8080
    nodePort: 31111
    protocol: TCP
  selector:
    app: *web
```
Specify same app name, so the node is connected to the container <br>
<br>
```
kubectl expose pod (name of pod) --name=...(Registered in DNS) --target-port=8080 --type=NodePort
```
If successful, message should say: service/... successful <br>
Nodeport ports range from 30000 - 32767 <br>
<br>

```
kubectl delete svc *servicename*
```
Deletes a service

## Creating a Service by using a Yaml file

```
apiVersion: v1
kind: Service
metadata:
  name: ps-nodeport (connected with DNS)
spec:
  type: NodePort
  ports:
  - port: 80
    targetPort: 8080
    nodePort: 31111
    protocol: TCP
  selector:
    app: web
```

### Definitions
* ClusterIP
* NodePort
* LoadBalancer 

Can do kubectl apply -f ...., where ... is a yaml file <br>

```
kubectl describe svc name (connected with DNS)
```
Use the describe command to describe running services

## Deployments
An object in the apps subgroup within the API <br>
Deployments are responsible for: Self-healing, scaling, rolling updates, rollbacks <br>
<br>
Containers -> Pods -> Replica Set (Scalability, reliability, desired state) -> Deployment (updates and rollbacks), another part of the infrastructure of how different objects work together in Kubernetes

## Create a Deployment Yaml
Check for deployments:
```
kubectl get deploy
```
Check for replica sets:
```
kubectl get rs
```
