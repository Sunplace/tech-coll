# Lws
https://github.com/kubernetes-sigs/lws

## ubuntu sleep example
apiVersion: leaderworkerset.x-k8s.io/v1
kind: LeaderWorkerSet
metadata:
  name: vllm
spec:
  replicas: 1 # 集群数量，一个集群
  leaderWorkerTemplate:
    size: 3 # 3: 一个leader，2个worker
    restartPolicy: RecreateGroupOnPodRestart
    leaderTemplate:
      metadata:
        labels:
          role: leader
      spec:
        containers:
          - name: vllm-leader
            image: ubuntu:latest
            command:
              - sh
              - -c
              - "sleep 100000"
    workerTemplate:
      spec:
        containers:
          - name: vllm-worker
            image: ubuntu:latest
            command:
              - sh
              - -c
              - "sleep 100000"