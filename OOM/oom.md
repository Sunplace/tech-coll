# OOM

## shell script to perform out of memory kill
```shell
#!/bin/sh
echo "app is running"
sleep 60
i=asdf
while true; do
  i="$i $i"
done
```