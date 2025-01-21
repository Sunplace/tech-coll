import time
import random
import prometheus_client as prom
from prometheus_client import start_http_server, Counter, Gauge

prom.REGISTRY.unregister(prom.PROCESS_COLLECTOR)
prom.REGISTRY.unregister(prom.PLATFORM_COLLECTOR)
prom.REGISTRY.unregister(prom.GC_COLLECTOR)

request_count = Counter('http_request_count', 'Number of HTTP requests')
request_latency = Gauge('http_request_latency_seconds', 'Latency of HTTP requests in seconds', labelnames=['method','path'])
random_number_metric = Gauge('random_number', 'Random number generated every 10 sec')

def update_metrics():
    while True:
        # 更新计数器和计数器
        request_count.inc()  # 每次循环增加请求计数
        request_latency.labels(method='GET', path='/health').set(1.0)  # 设置请求延迟
        request_latency.labels(method='POST', path='/data').set(2.0)  # 设置请求延迟
        random_number = random.randint(1, 10)
        random_number_metric.set(random_number)
        print('Random number is: ', random_number)
        time.sleep(10)  # 每秒更新一次

if __name__ == '__main__':
    # 启动一个 HTTP 服务器来暴露指标
    start_http_server(8000)
    # 启动另一个线程来定期更新指标
    import threading
    threading.Thread(target=update_metrics).start()