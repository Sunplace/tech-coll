# Linux

## ebtables
https://ebtables.netfilter.org/br_fw_ia/br_fw_ia.html

## ipvs, ipvsadm
https://sebastianczech.github.io/devops/2021/06/19/linux-virtual-server.html

## ipset
https://wiki.archlinux.org/title/Ipset

## conntrack
https://blog.cloudflare.com/conntrack-tales-one-thousand-and-one-flows/

## How do I check cgroup v2 is installed on my machine
https://unix.stackexchange.com/questions/471476/how-do-i-check-cgroup-v2-is-installed-on-my-machine

## linux ulimit
### memlock
https://unix.stackexchange.com/questions/449595/meaning-of-the-values-for-ulimit-memlock-flag

https://www.quora.com/What-is-Ulimit-Memlock

https://forums.oracle.com/ords/apexds/post/user-limit-memlock-in-limits-conf-on-linux-0373

### nproc
https://access.redhat.com/solutions/384633

https://unix.stackexchange.com/questions/322056/does-nproc-in-limits-conf-refers-to-number-of-processes-or-number-of-threads

### nofile
https://serverfault.com/questions/577437/what-is-the-impact-of-increasing-nofile-limits-in-etc-security-limits-conf

### 软限制与硬限制
https://access.redhat.com/solutions/384633

### iptables clear all rule
https://serverfault.com/questions/200635/best-way-to-clear-all-iptables-rules

iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
iptables -t nat -F
iptables -t mangle -F
iptables -t filter -F
iptables -t raw -F
iptables -t nat -X
iptables -t raw -X
iptables -t filter -X
iptables -t mangle -X

### ipvsadm clear all
ipvsadm --clear