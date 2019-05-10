FROM continuumio/miniconda3:latest

WORKDIR /app

ENV PATH /opt/conda/envs/env/bin:$PATH

RUN conda create --name WMH -y && \
    /bin/bash -c conda activate WMH && \
    conda install tensorflow-gpu=1.12.0 -y

RUN conda install scikit-learn -y && \
    conda install scikit-image -y && \
    conda install matplotlib -y

RUN pip install opencv-contrib-python && \
    conda install -c https://conda.anaconda.org/simpleitk SimpleITK -y && \
    conda install -c conda-forge nilearn -y && \
    pip install niftynet

RUN echo "source activate WMH" > ~/.bashrc

EXPOSE 8888
