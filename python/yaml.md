# PYYAML

```python
import yaml

##########################################################################################
# yaml - use folded block representation
# https://stackoverflow.com/questions/8640959/how-can-i-control-what-scalar-form-pyyaml-uses-for-my-data
##########################################################################################
def str_presenter(dumper: Any, data: Any) -> Any:
    if len(data.splitlines()) > 1:  # check for multiline string
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


yaml.add_representer(str, str_presenter)


do not use *idXXX and &idXXX for references
class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data: Any) -> bool:
        return True


# to use with safe_dump:
yaml.representer.SafeRepresenter.add_representer(str, str_presenter)
```

# ruamel.yaml

```python
from ruamel.yaml import YAML

yaml = YAML()

def str_representer(dumper: Any, data: Any) -> Any:
    if len(data.splitlines()) > 1:  # check for multiline string
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)

yaml.width = 4096  # prevent line-wrap
yaml.default_flow_style = False
yaml.indent(sequence=4, offset=2)
yaml.representer.add_representer(str, str_representer)
```
