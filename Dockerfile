# FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-runtime
FROM ccr.ccs.tencentyun.com/tione-public-images/ti-infer-gpu-base:1.0.0

WORKDIR /app
COPY . /app

COPY model_service.py /usr/local/service/adder/model_service.py
COPY entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

RUN pip install -r requirements.txt
ENV GRADIO_SERVER_PORT=7860
ENV GRADIO_SERVER_NAME=0.0.0.0
EXPOSE 7860
ENTRYPOINT ["python3", "server.py"]