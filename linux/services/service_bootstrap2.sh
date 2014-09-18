#!/usr/bin/env bash

cd "$( dirname "$0" )"

export KANASTARC="$( pwd )/settings.prod.py"

case "$1" in
    start)
        listen="$( (cat settings.prod.py ; echo 'print "%s:%s" % (HOST, PORT)') | python )"
        pid_file="$( pwd )".pid
        gunicorn -w 2 -p "$pid_file" -D --log-file=log/gunicorn.log -b "$listen" kanasta:app
    ;;
    stop)
        cat "$( pwd )".pid | xargs -r kill
    ;;
    reload)
        cat "$( pwd )".pid | xargs -r kill -HUP
    ;;

    *)
        echo "Eeee? I know just start, stop and reload commands" >&2
        exit 1
esac

exit 0
