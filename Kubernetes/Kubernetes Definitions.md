# Kubernetes

## Definitions
Masters - Also known as head nodes or the control plane <br>
Has many services its responsible for<br>
<br>
kube-apiserver - Front end to the control plane, exposes API, uses JSON/YAML files <br>
<br>
Cluster Store - Persists cluster store KV, based on etcd, performance is critical <br>
<br>
Kube-controller-manager - Controller of controllers, node controller, deployment controller, Endpoints/endpoint slice controller <br>
<br>
Kube Scheduler - Watches API server for new tasks <br>
<br>
Kubelet - Main Kubernetes agent, registers node with cluster, watches API server for work tasks, executes pods, reports back to master <br>
<br>
Container runtime <br>
<br>
Kube-proxy - <b>Networking</b> component, pod IP address, basic load balancing <br>
<br>
Containers always runs in pods <br>
<br>
Tightly coupled - When two containers (app services) absolutely need to share vols, memory etc <br>
<br>
Loosely coupled - When two containers (app services) don't absolutely need to share resources. For example, so there are two pods where each of them are in separate containers so they don't share resources  <br>
<br>
Scaling with pods <br>
<br>
App Container - <br>
Mesh container - <br>
Source: https://www.opsmx.com/blog/what-is-service-mesh-and-why-is-it-necessary/ <br>
<br>
Service - API (yaml), provides stable IP and DNS name <br>
Only sends traffic to healthy pods, send traffic to outside of cluser and can be TCP (default) or UDP <br>
<br>
Labels <br>
<br>
### K8's API and API Server
- Pod - Atomic unit of scheduling
- Rs - Replica count
- Deploy - Updates, rollbacks
- SVC - stable network abstraction
<br> These are called objects in the Kubernetes API <br>
Deployment  object definition:
- API sub-group [apps/v1]
- Replicas (integer)
- minReadySeconds (integer)
- progressDeadlineSeconds (integer)
- paused (boolean)
- revisionHistoryLimit (integer)
- selector (LabelSelector)
- strategy (DeploymentStrategy)
- template (PodTemplateSpec)

Objects Within API server:
- Pod
- Sts
- ds
- rs
- job
- cm
- deploy
- cronjob
- ep
- svc
- ing
- psp
- node
- secret

APIServer - Rest, Https, use Kubectl to configure and query apiserver <br>
<br>
K8's Cluster - Control plane, Worker nodes
