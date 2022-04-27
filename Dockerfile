FROM ubuntu:20.04

RUN apt update
RUN apt install -y sudo
RUN sudo apt update && sudo apt -y upgrade
RUN sudo apt install -y python3 && python3 -V && sudo apt install -y python3-pip
RUN sudo apt install -y python3-venv && python3 -m venv lung_env && . lung_env/bin/activate

RUN pip3 install keras nibabel scipy tensorflow matplotlib sklearn

RUN git clone https://github.com/rezazad68/BCDU-Net.git  /project

WORKDIR /project
CMD ["python3", "test.py"]