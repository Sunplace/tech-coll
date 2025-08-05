# Vllm

## 参数优化
--distributed-executor-backend=mp
--gpu-memory-utilization=1
--enforce-eager
--max-model-len=16384

## bitsandbyte 量化
>https://github.com/vllm-project/vllm/issues/4198

--quantization=bitsandbytes
--load-format=bitsandbytes

## multiple models running one gpu
https://github.com/vllm-project/vllm/issues/13633

https://github.com/vllm-project/vllm/issues/3326

https://github.com/vllm-project/vllm/issues/299

https://discuss.vllm.ai/t/does-vllm-support-deploy-multiple-docker-instance-on-one-gpu/657

https://discuss.vllm.ai/t/2-vllm-containers-on-a-single-gpu/608