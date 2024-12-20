# Yum mirror
  sed -e 's|^mirrorlist=|#mirrorlist=|g' \
      -e 's|^# baseurl=https://repo.almalinux.org|baseurl=https://mirrors.tencent.com|g' \
      -i.bak \
      /etc/yum.repos.d/almalinux*.repo