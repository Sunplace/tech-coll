FROM xinference:latest-2025-04-07
RUN mkdir /.xoscar
RUN chgrp -R 0 /.xoscar && \
    chmod -R g=u /.xoscar
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone