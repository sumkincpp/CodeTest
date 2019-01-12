
# Copying files by their full found path
```bash
find . -iname * | tr '\n' '\0' | xargs -n1 -0 cp -t .
```
