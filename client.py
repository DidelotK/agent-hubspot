from langgraph_sdk import get_client
import asyncio

client = get_client(url="http://localhost:2024")

async def main():
    async for chunk in client.runs.stream(
        None,  # Threadless run
        "hubspot-agent", # Name of assistant. Defined in langgraph.json.
        input={
          "messages": [{
              "role": "human",
              "content": "What is LangGraph?",
              }],
          "internal_knowledge": "The Keltio code is 1234567890",
        },
    ):
        print(f"Receiving new event of type: {chunk.event}...")
        print(chunk.data)
        print("\n\n")

asyncio.run(main())
