"""
Simple client to test our MCP server.

This demonstrates how to connect to and use the calculator server.
Run the server first: python simple_server.py
Then run this client: python test_client.py
"""

import asyncio
import os
from typing import Any, List

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import TextContent


def get_text_content(content_items: List[Any]) -> str:
    """Extract text content from MCP response."""
    for item in content_items:
        if isinstance(item, TextContent):
            return item.text
        elif hasattr(item, 'text'):
            return str(item.text)
    return str(content_items[0]) if content_items else "No content"


async def test_calculator_server():
    """Test the calculator server functionality."""
    # Create server parameters for stdio connection
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "python", "simple_server.py"],
        env=dict(os.environ),
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()
            print("✅ Connected to Simple Calculator Server")

            # List available tools
            tools = await session.list_tools()
            print(f"\n📊 Available tools: {len(tools.tools)}")
            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description}")

            # Test calculator tools
            print("\n🧮 Testing calculator tools:")
            
            # Test addition
            result = await session.call_tool("add", {"a": 15, "b": 27})
            print(f"  add(15, 27) = {get_text_content(result.content)}")
            
            # Test subtraction
            result = await session.call_tool("subtract", {"a": 100, "b": 42})
            print(f"  subtract(100, 42) = {get_text_content(result.content)}")
            
            # Test multiplication
            result = await session.call_tool("multiply", {"a": 6, "b": 7})
            print(f"  multiply(6, 7) = {get_text_content(result.content)}")
            
            # Test division
            result = await session.call_tool("divide", {"a": 84.0, "b": 2.0})
            print(f"  divide(84.0, 2.0) = {get_text_content(result.content)}")

            # List available resources
            resources = await session.list_resources()
            print(f"\n📚 Available resources: {len(resources.resources)}")
            for resource in resources.resources:
                print(f"  - {resource.uri}: {resource.description}")

            # Test reading resources
            print("\n📖 Reading resources:")
            
            # Read constants resource
            from mcp.types import AnyUrl
            resource = await session.read_resource(AnyUrl("data://constants"))
            print("  Constants:")
            print(f"    {get_text_content(resource.contents)}")
            
            # Test dynamic greeting resource
            resource = await session.read_resource(AnyUrl("greeting://Alice"))
            greeting = get_text_content(resource.contents)
            print(f"  Greeting for Alice: {greeting}")

            # List available prompts
            prompts = await session.list_prompts()
            print(f"\n💬 Available prompts: {len(prompts.prompts)}")
            for prompt in prompts.prompts:
                print(f"  - {prompt.name}: {prompt.description}")

            # Test math helper prompt
            prompt_result = await session.get_prompt("math_helper", {
                "problem": "Solve for x: 2x + 5 = 17",
                "style": "step-by-step"
            })
            print("\n📝 Math helper prompt:")
            for message in prompt_result.messages:
                if isinstance(message.content, TextContent):
                    print(f"    {message.content.text}")

            print("\n✅ All tests completed successfully!")


if __name__ == "__main__":
    asyncio.run(test_calculator_server())
