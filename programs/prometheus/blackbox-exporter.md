# Blackbox Exporter

```bash
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.labels.job=="dns-matrix-check-tcp") | .scrapeUrl'
"http://blackbox-exporter:9115/probe?module=dns_tcp&query_name=google.com&query_type=A&target=8.8.8.8%3A53"
...
```
