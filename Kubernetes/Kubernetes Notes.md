# Kubernetes

## Definitions
Masters - Also known as head nodes or the control plane <br>
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
Loosely coupled - When two containers (app services) don't absolutely need to share resources <br>
<br>
Scaling with pods <br>
<br>
App Container - <br>
Mesh container - <br>