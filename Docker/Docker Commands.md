# Docker Commands

1. Docker Login:
```
docker login
```

2. Build an Image:
```
docker build -t "registry"/"nameofapp" "directory"
```
"registry", "nameofapp" and "directory are placeholders. Name "registry" accordingly to the repository that the image will be pushed too and specify directory. If the files are in the current directory use a "." "registry" can also be replaced by an account username if an image is being pushed to a personal account to retrieve the image. 

3. Run the Image:
```
docker run -d -p port:port "registry"/"nameofapp"
```

4. Push the Image:
```
docker push "registry"/"nameofapp"
```

5. Pull an image:
```
docker pull "accountname"/"nameofapp"
```

6. Check Docker Images:
```
docker images
```

7.  Delete Docker Images:
```
docker rmi *dockerimageID*
```

```
docker rmi -f "dockerimageID"
```
-f means to forcibly delete the image every time. Instead or "dockerimageID", can specify the name of image to delete as well.

8. Look at current Docker containers:
```
docker container ls
```

```
docker ps -l
```
This command shows which containers are running on a default port.

9. Inspecting a Docker Container:
```
docker inspect "dockercontainerID"
```

10. Log in into an existing docker container (after it was created with the build command):
```
docker exec -it container_id /bin/bash
```
