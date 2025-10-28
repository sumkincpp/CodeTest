# uwsgi

- Emperor https://uwsgi-docs.readthedocs.io/en/latest/Emperor.html

- CLI Flags https://github.com/unbit/uwsgi/blob/master/core/uwsgi.c
- https://github.com/brunowego/cookbook/blob/develop/uwsgi.md?plain=1

## Tutorials

- Django ~ https://github.com/jrief/django-websocket-redis/blob/8aa0cbd37f1f19df2748bfc47d1154ad225f8f62/docs/running.rst#L226

## log-encoders

- https://uwsgi-docs.readthedocs.io/en/latest/LogEncoders.html
- https://github.com/search?q=log-encoder++path%3A**.ini&type=code
- https://blog.rama.io/json-logging-with-uwsgi

```ini
; https://www.velebit.ai/blog/tech-blog-uwsgi-json-logging/
; this will encode uwsgi messages into JSON, encode requests to JSON and leave application output unchanged
logger = default stdio
logger = applogger stdio
log-route = applogger {
log-route = default ^((?!\{).)*$
log-encoder = json:default {"time":"${micros}", "source":"uwsgi", "message":"${msg}"}
log-encoder = format:applogger ${msg}
log-encoder = nl
logger-req = stdio
log-format = "address":"%(addr)", "method":"%(method)", "protocol":"%(proto)", "resp_size":%(size), "req_body_size":%(cl), "resp_status":%(status), "resp_time":%(secs)"
log-req-encoder = format {"time":"${micros}", "source":"uwsgi-req", ${msg}}
log-req-encoder = nl
```