from typing import TypedDict, Annotated, Optional
from langgraph.graph.message import add_messages
from operator import add

class Input(TypedDict):
    message: str

class State(TypedDict):
    """Input state for the agent.

    Defines the initial structure of incoming data.
    See: https://langchain-ai.github.io/langgraph/concepts/low_level/#state
    """
    messages: Annotated[list, add_messages] = []
