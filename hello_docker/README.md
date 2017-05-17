To run simple "Hello Docker" application at your machine you should:
- Being in working directory with Dockerfile
- Build an image from Dockerfile:
    sudo docker build -t artemkhymenko/hello_docker .
- Run a container:
    sudo docker run -it artemkhymenko/hello_docker

* "artemkhymenko/hello_docker" - is an example image's name, you can use your own
