# Podman Commands

```
podman image ls
```
List images

```
podman ps
```
List containers

```
podman ps -a
```
List all containers, including ones that are deleted

```
podman run --name="" -d -p 8080:80 imagename
```
Running an image, "imagename" is the name of the image and the empty "" is how the script is executed. In the "" placeholder, /bin/bash can be written there for example. 8080:80 are placeholder ports. 

```
podman pull ...
```
Pull an image

```
podman pull docker.io/"imagename"
```
Pull a docker image using podman. Statement must begin with "docker.io/". For further help use the official Podman documentation: https://podman.io/getting-started/

```
podman push "imagename"
```
Push an image

```
podman build -t imagename .
```
Building an image. Podman build documentation: https://docs.podman.io/en/latest/markdown/podman-build.1.html
