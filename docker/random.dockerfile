FROM alpine
RUN apk update
RUN apk add openssl
RUN time openssl rand 1000000000 | head -c 356000000 > /root/356M