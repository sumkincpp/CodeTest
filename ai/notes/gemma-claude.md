# Gemma in llama.cpp with Claude

## Start llama.cpp server

```bash
$ llama-server -hf ggml-org/gemma-4-E2B-it-GGUF --host 0.0.0.0
```

## Configure current project

```bash
$ cat .claude/settings.local.json
{
  "env": {
    "ANTHROPIC_BASE_URL": "http://192.168.56.1:8080"
  },
  "model": "gemma4",
  "permissions": {
    "allow": [
      "Bash(python:*)"
    ]
  }
}
```

## & run

```
$ claude
```

## Resources

- See https://x.com/PawelHuryn/status/2040519790779900075