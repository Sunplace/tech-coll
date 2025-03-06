# Docker

## docker build via proxy
docker build --build-arg http_proxy=http://192.168.56.101:8080/ --build-arg https_proxy=http://192.168.56.101:8080/ -t localhost:latest -f dockerfile .