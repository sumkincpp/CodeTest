
Some interesting PromQL queries
```
rate(some_rated_data[5m])/(rate(some_rated_data[5m]) + 0.0001)
up or on() vector(0)
```
