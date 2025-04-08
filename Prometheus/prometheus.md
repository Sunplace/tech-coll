# Prometheus
## how many time series
https://serverfault.com/questions/817424/how-to-find-out-the-number-of-time-series-stored-in-prometheus-leveldb
**prometheus_tsdb_head_series**
**count({__name__=~".+"})**

## how many datapoint
https://docs.victoriametrics.com/metricsql/#count_over_time

https://stackoverflow.com/questions/70950899/get-datapoint-count-of-a-prometheus-timeseries

**count_over_time(some_metric[1h])**