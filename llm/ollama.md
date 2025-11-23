# Ollama

## Windows - Update all local models

```bash
$ ollama ls | Select-Object -Skip 1 | % { ($_ -split '\s+')[0] } | % { "ollama pull $_" }
ollama pull llama3.1:latest
ollama pull gemma3:4b
ollama pull qwen3-coder:30b
ollama pull nomic-embed-text:latest
ollama pull qwen3-coder:latest
ollama pull qwen3:4b
ollama pull qwen3:8b

$ ollama ls | Select-Object -Skip 1 | % { ($_ -split '\s+')[0] } | % { ollama pull $_ }
...
```
