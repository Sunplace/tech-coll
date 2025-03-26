#!/bin/bash


# Author: peter
# Date: 2025-03-19 21:53
# create a wireguard instance

set -e
set -x

## install required package
apt update -y && apt install wireguard curl privoxy
sed -i '/^listen-address/d' /etc/privoxy/config
echo "listen-address 0.0.0.0:8118" >> /etc/privoxy/config
systemctl enable --now privoxy

## get public ip
PUBLIC_IP=$(curl https://ipinfo.io/ip)

## change to workdir
mkdir -p /etc/wireguard
cd /etc/wireguard

## generate server key.
wg genkey | (umask 0077 && tee server.key) | wg pubkey > server.pub
SERVER_KEY=$(cat server.key)
SERVER_PUB=$(cat server.pub)

## generate client key.
wg genkey | (umask 0077 && tee client.key) | wg pubkey > client.pub
CLIENT_KEY=$(cat client.key)
CLIENT_PUB=$(cat client.pub)

## generate wireguard server configuration
cat > wg-server.conf <<EOF
[Interface]
Address = 10.0.222.1/24
ListenPort = 54312
PrivateKey = $SERVER_KEY

[Peer]
PublicKey = $CLIENT_PUB
AllowedIPs = 10.0.222.2/32
PersistentKeepalive =25
EOF

## generate wireguard client configuration
cat > wg-client.conf <<EOF
[Interface]
Address = 10.0.222.2/24
ListenPort = 12345
PrivateKey = $CLIENT_KEY

[Peer]
PublicKey = $SERVER_PUB
AllowedIPs = 10.0.222.1/32
PersistentKeepalive =25
Endpoint = $PUBLIC_IP:16000
EOF

## set ip forward enable
sysctl -w net.ipv4.conf.all.forwarding=1

## set iptables masquerade
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

## iptable: open port range
iptables -t nat -I PREROUTING -i eth0 -p udp -m multiport --dports 16000:17000 -j REDIRECT --to-ports 54312