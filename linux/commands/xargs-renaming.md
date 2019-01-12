
# Renaming file according to the pattern

```bash
ls *.srt | \
awk -F'.' '{ res=toupper($1)"."tolower($2)".subs"; for(i=3;i<=NF;++i) { res = res"."$i; }; print "mv "$0" "res; }' | \
tr '\n' '\0' | xargs -0 -n1 -I{} sh -c "{}"
```
