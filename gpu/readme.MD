docker build .
docker run --runtime=nvidia -d --name VBTIDockerGPU -p 8000:8888 -v <PATH_TO_PROJECT>:/home/shared vbti:v0.0.3-gpu

Check localhost:8000 and enjoy
