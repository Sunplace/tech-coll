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