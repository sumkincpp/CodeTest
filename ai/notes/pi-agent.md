### List available models

```bash
pi --list-models
```

### Start an interactive conversation with a specific model and prompt

```bash
pi --provider ollama --model "qwen3.5:0.8b" "Explain this repository"
```

### Run once, print the final answer, and exit

```bash
pi --provider ollama --model "qwen3.5:0.8b" -p "Explain this repository"
```

### Include input from a file

```bash
pi --provider ollama --model "qwen3.5:0.8b" -p @input.txt "Summarize this"
```

### Save conversation events as a JSONL trace

```bash
pi --provider ollama --model "qwen3.5:0.8b" --mode json "Explain this repository" > trace.jsonl
```

These examples assume Pi has a configured provider named `ollama` with the model `qwen3.5:0.8b`. Use the provider and model IDs shown by `pi --list-models`.
