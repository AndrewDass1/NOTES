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
podman tag "imagename" "newimagename"
```
Rename an existing image under a new name. The image with its old name will remain and the image with its new name will be created. 

```
podman build -t imagename .
```
Building an image. Podman build documentation: https://docs.podman.io/en/latest/markdown/podman-build.1.html

```
podman run --name="" -d -p 8080:80 imagename
```
Running an image, "imagename" is the name of the image and the empty "" is the new name given to the container. 8080:80 are placeholder ports. 

## Container Commands
```
podman stop containername
```

```
podman restart containername
```

```
podman kill containername
```
containerID can be used instead of containername

```
podman rm containername
```
Delete a container
```
podman rm -f containername
```
Forcibly delete a container

```
podman rmi imagename
```
Remove an image, can use imageid instead of imagename

```
podman rmi -f imagename
```
Forcibly delete an image
