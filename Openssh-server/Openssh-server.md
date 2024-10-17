# Openssh-server

## sshd run as normal user
https://serverfault.com/questions/344295/is-it-possible-to-run-sshd-as-a-normal-user
https://superuser.com/questions/1547888/is-sshd-hard-coded-to-require-root-access

ssh-keygen -f ssh_host_rsa_key -N '' -t rsa

cat << EOF > sshd_config
Port 2222
HostKey /home/jovan/ssh/ssh_host_rsa_key
AuthorizedKeysFile  /home/jovan/.ssh/authorized_keys
ChallengeResponseAuthentication no
UsePAM no
PidFile /home/jovan/ssh/sshd.pid
EOF

# Update ubuntu base image and install basic tools
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update --yes && \
    apt-get upgrade --yes && \
    apt-get install --yes --no-install-recommends \
    curl \
#    tini \
    wget \
    ca-certificates \
#    sudo \
    locales && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen