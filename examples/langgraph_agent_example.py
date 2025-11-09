from stackifier import TraceHook, FileWriter, LangGraphTracer
from typing import TypedDict, Annotated
import operator

trace = TraceHook(storage=FileWriter(path="logs/langgraph_agent.jsonl"))
tracer = LangGraphTracer(trace)


class State(TypedDict):
    messages: Annotated[list, operator.add]
    graph_id: str
    step: int


def agent_node(state: State):
    graph_id = state.get("graph_id", "default")
    step = state.get("step", 0)
    
    tracer.log_node_start(
        graph_id=graph_id,
        node_name="agent_node",
        step_index=step,
        inputs={"messages": state["messages"]}
    )
    
    new_message = {
        "role": "assistant",
        "content": "Processing your request..."
    }
    
    result = {
        "messages": [new_message],
        "step": step + 1
    }
    
    tracer.log_node_end(
        graph_id=graph_id,
        step_index=step,
        outputs=result
    )
    
    return result


def tool_node(state: State):
    graph_id = state.get("graph_id", "default")
    step = state.get("step", 0)
    
    tracer.log_node_start(
        graph_id=graph_id,
        node_name="tool_node",
        step_index=step,
        inputs={"messages": state["messages"]}
    )
    
    tool_result = {
        "role": "tool",
        "content": "Tool execution result"
    }
    
    result = {
        "messages": [tool_result],
        "step": step + 1
    }
    
    tracer.log_node_end(
        graph_id=graph_id,
        step_index=step,
        outputs=result
    )
    
    return result


def run_graph_example():
    import uuid
    
    initial_state = {
        "messages": [{"role": "user", "content": "Hello, I need help"}],
        "graph_id": str(uuid.uuid4()),
        "step": 0
    }
    
    state = agent_node(initial_state)
    
    state["graph_id"] = initial_state["graph_id"]
    final_state = tool_node(state)
    
    trace.flush()
    
    print(f"Graph execution complete. Logged to logs/langgraph_agent.jsonl")
    print(f"Graph ID: {initial_state['graph_id']}")
    print(f"Total steps: {final_state['step']}")


if __name__ == "__main__":
    run_graph_example()
