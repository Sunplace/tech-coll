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