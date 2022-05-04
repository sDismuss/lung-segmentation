FROM ubuntu:20.04

WORKDIR /workdir

RUN apt update && apt install -y sudo
RUN sudo apt update && sudo apt -y upgrade
RUN sudo apt install -y python3 \
                        python3-venv \
                        python3-pip \
                        git

RUN python3 -m venv lung_env && . lung_env/bin/activate
RUN pip3 install keras \
                 nibabel \
                 scipy \
                 tensorflow \
                 matplotlib \
                 sklearn

COPY . /workdir

RUN python3 test.py