FROM z5/cuda-conda
ENV PATH=$PATH:/root/anaconda3/bin/
ENV PY.THONUNBUFFERED=1
RUN apt-get update && apt-get install -y
RUN apt-get install libgl1-mesa-glx -y
COPY . /app
ADD environment.yml /tmp/environment.yml
WORKDIR /app
RUN conda env create -f /tmp/environment.yml
ENV PATH /root/anaconda3/envs/ppn2vEnv/bin:$PATH
RUN /bin/bash -c "source activate anom_env"
WORKDIR /app/src/code
#CMD ["python", "main.py"]
CMD ["./run.sh"]
