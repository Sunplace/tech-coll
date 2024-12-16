# Openshift Container Platform

## fix permission
https://stackoverflow.com/questions/58473832/how-do-i-change-the-permissions-in-openshift-container-platform

https://docs.openshift.com/container-platform/4.16/openshift_images/create-images.html

```dockerfile
from xxx:xxx
USER root
RUN chgrp -R 0 /home && chmod -R g=u /home
```

## pod security
https://github.com/rook/rook/issues/11755