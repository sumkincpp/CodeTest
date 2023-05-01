# Removing BOM

BOM (Byte Order Mark) - M-oM-;M-?^M 

```python
string = "\ufeffHello World!"
string = string.replace("\ufeff", "")
print(string)
```

```python
with open(file, encoding="utf-8-sig") as fd:
  data = fd.read()
```
