# Stackifier

Lightweight data collection library for WhatsApp AI agents - log conversations, tool calls, and metrics to JSONL or S3 with OpenAI-compatible schema.

## Quick Start

```bash
pip install stackifier
```

```python
from stackifier import TraceHook, FileWriter

trace = TraceHook(storage=FileWriter(path="logs/conversations.jsonl"))

trace.log_message(role="user", content="Hello! What's the weather?")
trace.log_message(role="assistant", content="Let me check that for you.")
trace.flush()
```

## Documentation

For full documentation, examples, and API reference, see the [README.md](../README.md) in the project root.

## Features

- **OpenAI Chat Schema**: Store every turn using standard `{system,user,assistant,tool}` roles
- **Local First**: Append to JSONL files by default, zero-ops setup
- **S3 Optional**: Drop-in cloud storage with boto3
- **WhatsApp Adapters**: Normalize Meta Cloud API and Twilio webhooks
- **LLM Integrations**: Native support for LiteLLM, LangChain, LangGraph, OpenRouter
- **Rich Metrics**: Capture timing, tokens, costs, tool latencies

## Links

- [GitHub Repository](https://github.com/BryanTheLai/stackifier)
- [PyPI Package](https://pypi.org/project/stackifier/)
- [Installation & Usage](../README.md)
