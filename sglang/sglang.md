# Sglang

## install
>https://docs.sglang.ai/start/install.html

## check env
python3 -m sglang.check_env

## run
>https://github.com/sgl-project/sglang/issues/748

python3 -m sglang.launch_server --model-path /root/hf_model/Qwen/Qwen2-72B-Instruct-GPTQ-Int4 --dtype half --trust-remote-code --tp-size 4 --disable-flashinfer

>https://docs.sglang.ai/backend/send_request.html