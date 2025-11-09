from stackifier import TraceHook, FileWriter, LiteLLMTracer
import time

trace = TraceHook(storage=FileWriter(path="logs/litellm_conversations.jsonl"))
tracer = LiteLLMTracer(trace)


def chat_with_litellm():
    try:
        import litellm
    except ImportError:
        print("LiteLLM not installed. Install with: pip install litellm")
        return
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
    
    start = time.time()
    
    response = litellm.completion(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    tracer.log_completion(messages, response, start, model="gpt-3.5-turbo")
    trace.flush()
    
    print(f"Response: {response.choices[0].message.content}")
    print(f"Logged conversation to logs/litellm_conversations.jsonl")


def chat_with_tool_calls():
    try:
        import litellm
    except ImportError:
        print("LiteLLM not installed. Install with: pip install litellm")
        return
    
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get the current weather",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "City name"
                        }
                    },
                    "required": ["location"]
                }
            }
        }
    ]
    
    messages = [
        {"role": "user", "content": "What's the weather in Paris?"}
    ]
    
    start = time.time()
    
    response = litellm.completion(
        model="gpt-4",
        messages=messages,
        tools=tools
    )
    
    tracer.log_completion(messages, response, start, model="gpt-4")
    
    if response.choices[0].message.tool_calls:
        tool_call = response.choices[0].message.tool_calls[0]
        
        messages.append({
            "role": "assistant",
            "content": None,
            "tool_calls": [tool_call]
        })
        
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": tool_call.function.name,
            "content": "Sunny, 22°C"
        })
        
        start = time.time()
        final_response = litellm.completion(
            model="gpt-4",
            messages=messages
        )
        
        tracer.log_completion(messages, final_response, start, model="gpt-4")
    
    trace.flush()
    print(f"Logged tool-calling conversation to logs/litellm_conversations.jsonl")


if __name__ == "__main__":
    print("Choose an example:")
    print("1. Simple chat")
    print("2. Chat with tool calls")
    
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == "1":
        chat_with_litellm()
    elif choice == "2":
        chat_with_tool_calls()
    else:
        print("Invalid choice")
