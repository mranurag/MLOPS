FROM continuumio/anaconda3
ENV PATH=$PATH:/root/anaconda3/bin/
ENV PY.THONUNBUFFERED=1
RUN apt-get update && apt-get install -y
RUN apt-get install libgl1-mesa-glx -y
COPY . /app
ADD environment.yml /tmp/environment.yml
WORKDIR /app
RUN conda install -c conda-forge streamlit
RUN conda install flask
WORKDIR /app/src/code
