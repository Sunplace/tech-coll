# Redhat

## redhat 常用包
yum install curl wget unzip tar vim less iputils tcpdump telnet tree net-tools iproute bind-utils

## yum download only
```shell
yum install zabbix-proxy-mysql zabbix-sql-scripts zabbix-selinux-policy zabbix-agent zabbix-agent2 MariaDB-server MariaDB-client
yumdownloader --destdir=/tmp/nginx-deps --resolve nginx
yumdownloader --destdir=/root/zabbix-mariadb-deps-mindray --resolve zabbix-proxy-mysql zabbix-sql-scripts zabbix-selinux-policy zabbix-agent zabbix-agent2 MariaDB-server MariaDB-client zabbix-get zabbix-sender
```
