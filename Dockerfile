FROM ubuntu:20.04
RUN apt update && apt -y upgrade && apt -y install bash python3 python3-pip python3-venv
RUN pip3 -m venv lung_env && . lung_env/bin/activate
RUN pip3 install keras nibabel scipy tensorflow matplotlib sklearn
RUN git clone https://github.com/rezazad68/BCDU-Net.git  /project
WORKDIR /project
CMD ["python3", "test.py"]