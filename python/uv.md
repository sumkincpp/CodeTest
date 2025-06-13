# astral-sh/uv

Install for all users (/usr/local/bin)

```bash
sudo curl -LsSf https://astral.sh/uv/install.sh | sudo env UV_INSTALL_DIR="/usr/local/bin/" sh
```

Install python tool to custom folder

```bash
UV_TOOL_BIN_DIR=/usr/local/bin uv tool install foo
```
