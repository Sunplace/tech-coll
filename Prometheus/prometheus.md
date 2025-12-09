# Prometheus
## how many time series
https://serverfault.com/questions/817424/how-to-find-out-the-number-of-time-series-stored-in-prometheus-leveldb
**prometheus_tsdb_head_series**
**count({__name__=~".+"})**

## how many datapoint
https://docs.victoriametrics.com/metricsql/#count_over_time

https://stackoverflow.com/questions/70950899/get-datapoint-count-of-a-prometheus-timeseries

**count_over_time(some_metric[1h])**

## how much data disk usage
https://stackoverflow.com/questions/69738250/how-to-calculate-current-prometheus-tsdb-storage-size-from-tsdb-status-url

**prometheus_tsdb_storage_blocks_bytes / 1024 / 1024**

## prometheus reload
https://prometheus.io/docs/guides/basic-auth/

https://stackoverflow.com/questions/78379984/how-to-reload-prometheus-config-without-restarting

## prometheus alert rule special time
https://stackoverflow.com/questions/69717672/time-based-alerts-in-prometheus-alertmanager

win_script_backups_status{endpoint=~".*", name="BackupLog_succeeded"} == 0  and on() ((hour() == 4 and minute() < 30) or (hour() == 16 and minute() < 30))

## prometheus 无数据
https://signoz.io/guides/time-series-from-prometheus-source-how-to-set-nulls-as-zero/

## How to find out the number of time series stored in Prometheus LevelDB
https://serverfault.com/questions/817424/how-to-find-out-the-number-of-time-series-stored-in-prometheus-leveldb
