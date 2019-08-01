#  ___      ___ ________  _________  ___      #
# |\  \    /  /|\   __  \|\___   ___\\  \     #
# \ \  \  /  / | \  \|\ /\|___ \  \_\ \  \    #
#  \ \  \/  / / \ \   __  \   \ \  \ \ \  \   #
#   \ \    / /   \ \  \|\  \   \ \  \ \ \  \  #
#    \ \__/ /     \ \_______\   \ \__\ \ \__\ #
#     \|__|/       \|_______|    \|__|  \|__| #
#                                             #
#        YOUR  AI  INNOVATION  PARTNER        #

FROM nvidia/cuda:10.0-cudnn7-runtime-ubuntu18.04

# Prevent asking for input during setup
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Amsterdam

LABEL version="0.0.3-gpu"
LABEL vendor="VBTI"
LABEL url="https://vbti.nl"

# Update, and install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        # Python
        python3-setuptools \
        python3-dev \
		python3-tk \
		python3-pip \
		# Imgaug
		libgtk2.0-dev \
		# OpenAI Gym
		zlib1g-dev \
		libjpeg-dev \
		cmake \
		swig \
		python-pyglet \
		python3-opengl \
		libboost-all-dev \
		libsdl2-dev \
        libosmesa6-dev \
        patchelf \
        ffmpeg \
        xvfb \
		&& \
	apt-get clean && \
	apt-get autoremove -y

# Install Python modules
RUN pip3 install --no-cache-dir --upgrade \
        numpy \
        jupyterlab \
        ipywidgets \
        scipy \
        scikit-learn \
        pandas \
        matplotlib \
        opencv-contrib-python \
        imutils \
        imgaug \
        h5py \
        seaborn \
        Pillow \
        nltk \
        imbalanced-learn \
        gym \
        atari-py \
        tf-nightly-gpu \
        keras

# Enable Jupyter widgets
RUN jupyter nbextension enable --py widgetsnbextension

# Change Jupyter directory
RUN mkdir -p /root/.jupyter && \
    echo "c.NotebookApp.notebook_dir = '/home'" >> ~/.jupyter/jupyter_notebook_config.py && \
    # !!! INSECURE !!!
    echo "c.NotebookApp.token = ''" >> ~/.jupyter/jupyter_notebook_config.py
    # !!! INSECURE !!!

# Include files
COPY ./include /home

# Run Jupyter and allow connection through port 8888
EXPOSE 8888
CMD xvfb-run -a jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
