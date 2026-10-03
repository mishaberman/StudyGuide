"""A real MCP server and client, using an in-process transport without an API key."""
import asyncio
import importlib
from fastmcp import FastMCP, Client

server = FastMCP('Synthetic workshop catalog')
lookup = importlib.import_module('labs.04_tool_loop').lookup_lab

@server.tool()
def lookup_workshop(slug: str) -> dict:
    """Read a synthetic workshop: messages, tools, or evals."""
    return lookup(slug)

async def demo():
    async with Client(server) as client:
        print('MCP tools:', [t.name for t in await client.list_tools()])
        result = await client.call_tool('lookup_workshop', {'slug': 'tools'})
        print(result.data)
        return result.data

if __name__ == '__main__':
    asyncio.run(demo())
