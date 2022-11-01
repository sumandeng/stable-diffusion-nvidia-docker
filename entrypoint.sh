#!/bin/bash
source /etc/profile
source /root/.bashrc
export LD_LIBRARY_PATH=/usr/local/python3/lib/python3.8/site-packages/torch/lib:/usr/local/openmpi/lib:/usr/local/nccl/lib:/usr/local/cuda/lib64:/usr/local/python3/lib:/usr/local/python3/lib64:/usr/local/openmpi/lib:/usr/local/gcc/lib:/usr/local/gcc/lib64

MODEL_DIR=/data/model
ALGORITHM_NAME=m
REST_PORT=8501

echo "================== code path ${MODEL_DIR}=========="
cd ${MODEL_DIR}

if [ -f "requirements.txt" ]; then
  echo "============== install python requirements   ===================="
  echo "python3 -m pip install -r requirements.txt"
  python3 -m pip install -r requirements.txt
  echo "============== install python requirements done ================="
fi

echo "====================== start serving ============================"
echo "python3 -m tiinfer --http_port ${REST_PORT} --algorithm_name ${ALGORITHM_NAME} --model_dir ${MODEL_DIR} "
python3 -m tiinfer --http_port ${REST_PORT} --algorithm_name "${ALGORITHM_NAME}" --model_dir ${MODEL_DIR}