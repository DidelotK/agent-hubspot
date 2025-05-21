from __future__ import annotations


from langgraph.graph import START, MessagesState, StateGraph

from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from langgraph.prebuilt import ToolNode, tools_condition

from agent.models import State
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.store.memory import InMemoryStore
from agent.tools import get_hubspot_contacts, get_hubspot_transactions
from langgraph.store.base import BaseStore
from langchain_core.runnables.config import RunnableConfig


checkpointer = InMemorySaver()
# store = InMemoryStore()


tavily_search_tool = TavilySearch(max_results=2)
tools = [tavily_search_tool, get_hubspot_contacts, get_hubspot_transactions]

llm = init_chat_model("openai:gpt-4.1")
llm_with_tools = llm.bind_tools(tools)
user_id = "1"
namespace_for_internal_knowledge = (user_id, "internal_knowledge")


def chatNode(state: MessagesState, config: RunnableConfig, store: BaseStore):
    data = {}
    user_id = config["configurable"]["user_id"]
    print(f"user_id: {user_id}")
    print(store)
    print(store.get(namespace_for_internal_knowledge, "profile"))

    store.put(namespace_for_internal_knowledge, "profile", {"name": "John Doe", "age": 30})

    if "messages" in state:
        data["messages"] = llm_with_tools.invoke(state["messages"])

    return data


tool_node = ToolNode(tools=tools)
graph = (
    StateGraph(MessagesState)
    .add_node("chatbot", chatNode)
    .add_node("tools", tool_node)
    .add_conditional_edges(
        "chatbot",
        tools_condition,
    )
    .add_edge("tools", "chatbot")
    .add_edge(START, "chatbot")
    .compile()
)

# La première fois que l'agent est lancé, il va demander à l'utilisateur des informations sur sa façon de gérer son CRM