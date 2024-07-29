# Http proxy

## http proxy environment variables
export http_proxy=http://10.203.0.1:5187/
export https_proxy=$http_proxy
export ftp_proxy=$http_proxy
export rsync_proxy=$http_proxy
export no_proxy="localhost,127.0.0.1,localaddress,.localdomain.com"

export HTTP_PROXY=http://10.203.0.1:5187/
export HTTPS_PROXY=$http_proxy
export FTP_PROXY=$http_proxy
export RSYNC_PROXY=$http_proxy
export NO_PROXY="localhost,127.0.0.1,localaddress,.localdomain.com"