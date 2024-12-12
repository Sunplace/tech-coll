# TCP time wait

## 介绍
主动断开连接的一方都会进入这个状态。正常状态。
如果服务端遭遇大量短连接，并且都是主动断开连接，那可能会产生大量的time wait。

https://en.wikipedia.org/wiki/Transmission_Control_Protocol

https://totozhang.github.io/2016-01-31-tcp-timewait-status/

https://en.wikipedia.org/wiki/File:Tcp_state_diagram_fixed.svg

## 查看 以及 分析
ss --numeric -o state time-wait dst 192.168.56.0/24

ss -ntap

https://stackoverflow.com/questions/1803566/what-is-the-cost-of-many-time-wait-on-the-server-side

https://serverfault.com/questions/23385/huge-amount-of-time-wait-connections-says-netstat

https://serverfault.com/questions/478691/avoid-time-wait-connections

https://serverfault.com/questions/329845/how-to-forcibly-close-a-socket-in-time-wait

## time wait 的超时时间是硬编码在系统中，默认60s
ss --numeric -o state time-wait dst 192.168.56.0/24

https://serverfault.com/questions/23385/huge-amount-of-time-wait-connections-says-netstat

## 缓解措施，最好不要使用，有害处。
https://stackoverflow.com/questions/6426253/tcp-tw-reuse-vs-tcp-tw-recycle-which-to-use-or-both

## 深度分析
https://totozhang.github.io/2016-01-31-tcp-timewait-status/