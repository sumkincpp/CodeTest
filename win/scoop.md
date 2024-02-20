
# scoop update all

- https://github.com/ScoopInstaller/Scoop/issues/3954

```bash
scoop list | foreach { scoop update $_.Name }
```
