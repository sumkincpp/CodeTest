# astral-sh/uv

## pyproject.toml

```toml
[project]
name = "paper-pi0"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "lgpio",
    "requests",
    "pillow",
    "waveshare-epd",
]

[tool.uv.sources]
waveshare-epd = { path = "lib/waveshare_epd", editable = true }
```

## commands

Install for all users (/usr/local/bin)

```bash
sudo curl -LsSf https://astral.sh/uv/install.sh | sudo env UV_INSTALL_DIR="/usr/local/bin/" sh
```

Install python tool to custom folder

```bash
UV_TOOL_BIN_DIR=/usr/local/bin uv tool install foo
```

adding editable library

```
uv pip install -e add path_to_local_project
```
