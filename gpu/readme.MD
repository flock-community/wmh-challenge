docker build .
docker run --runtime=nvidia -d --name VBTIDockerGPU -p 8000:8888 -v <PATH_TO_PROJECT>:/home/shared vbti:v0.0.3-gpu

sudo docker run --gpus all nvidia/cuda:9.0-base nvidia-smi

Check localhost:8000 and enjoy
