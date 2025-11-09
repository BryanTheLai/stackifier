# Stackifier Examples

This directory contains practical examples of using Stackifier for data collection in different scenarios.

## Examples Overview

### 1. WhatsApp Agent Example (`whatsapp_agent_example.py`)

FastAPI webhook integration for WhatsApp agents using both Meta Cloud API and Twilio.

**Features:**
- Meta WhatsApp webhook handler
- Twilio webhook handler
- Agent message logging

**Run:**
```bash
pip install fastapi uvicorn
python examples/whatsapp_agent_example.py
```

### 2. LangGraph Agent Example (`langgraph_agent_example.py`)

Demonstrates logging LangGraph node executions with step-level tracking.

**Features:**
- Agent node logging
- Tool node logging
- Graph step tracking
- Multi-node execution flow

**Run:**
```bash
python examples/langgraph_agent_example.py
```

### 3. LiteLLM Example (`litellm_example.py`)

Shows how to log LiteLLM completions including tool calling.

**Features:**
- Simple chat completion
- Tool calling with function execution
- Token and timing metrics

**Run:**
```bash
pip install litellm
python examples/litellm_example.py
```

## Output

All examples log to the `logs/` directory in JSONL format. Each log file contains:
- OpenAI-compatible message format
- Timing metrics
- Token usage
- Custom metadata

## Integration with Your Project

To integrate Stackifier into your existing project:

1. **Install Stackifier:**
   ```bash
   pip install stackifier
   ```

2. **Import and initialize:**
   ```python
   from stackifier import TraceHook, FileWriter
   trace = TraceHook(storage=FileWriter(path="logs/my_agent.jsonl"))
   ```

3. **Log events:**
   ```python
   trace.log_message(role="user", content="Hello")
   trace.log_message(role="assistant", content="Hi there!")
   trace.flush()
   ```

4. **For specific integrations, use the appropriate tracer:**
   - LiteLLM: `LiteLLMTracer`
   - LangChain: `LangChainTracer`
   - LangGraph: `LangGraphTracer`
   - OpenRouter: `OpenRouterTracer`

## Best Practices

1. **Always call `flush()`** at the end of conversations or before app shutdown
2. **Use conversation IDs** to group related messages
3. **Add custom metadata** for filtering and analysis
4. **Set up proper error handling** around trace operations
5. **Use buffering** for high-throughput scenarios (automatically enabled)

## Questions?

Check the main [README.md](../README.md) for full API documentation and more examples.
