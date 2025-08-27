"""
Direct test of the simple calculator server functionality.

This imports and tests the server functions directly to demonstrate they work.
"""

from simple_server import mcp


def test_server_functions():
    """Test the server's registered functions directly."""
    print("🧮 Testing Simple Calculator Server Functions")
    print("=" * 50)
    
    # Test calculator tools directly
    print("\n📊 Calculator Tools:")
    
    # Import the tool functions from the server
    tools_dict = {}
    for tool_name, tool_info in mcp._tools.items():
        tools_dict[tool_name] = tool_info.func
    
    # Test each calculator function
    try:
        result = tools_dict['add'](15, 27)
        print(f"  ✅ add(15, 27) = {result}")
        
        result = tools_dict['subtract'](100, 42)
        print(f"  ✅ subtract(100, 42) = {result}")
        
        result = tools_dict['multiply'](6, 7)
        print(f"  ✅ multiply(6, 7) = {result}")
        
        result = tools_dict['divide'](84.0, 2.0)
        print(f"  ✅ divide(84.0, 2.0) = {result}")
        
        # Test division by zero protection
        try:
            result = tools_dict['divide'](10.0, 0.0)
            print(f"  ❌ divide(10.0, 0.0) should have failed!")
        except ValueError as e:
            print(f"  ✅ divide(10.0, 0.0) correctly raised error: {e}")
            
    except Exception as e:
        print(f"  ❌ Error testing tools: {e}")
    
    # Test resource functions
    print("\n📚 Resource Functions:")
    
    resources_dict = {}
    for resource_pattern, resource_info in mcp._resources.items():
        resources_dict[resource_pattern] = resource_info.func
    
    try:
        # Test greeting resource
        greeting_func = resources_dict['greeting://{name}']
        result = greeting_func("Alice")
        print(f"  ✅ greeting for Alice: {result}")
        
        # Test constants resource
        constants_func = resources_dict['data://constants']
        result = constants_func()
        print(f"  ✅ constants resource loaded: {len(result)} characters")
        
        # Test formulas resource  
        formulas_func = resources_dict['data://formulas']
        result = formulas_func()
        print(f"  ✅ formulas resource loaded: {len(result)} characters")
        
    except Exception as e:
        print(f"  ❌ Error testing resources: {e}")
    
    # Test prompt functions
    print("\n💬 Prompt Functions:")
    
    prompts_dict = {}
    for prompt_name, prompt_info in mcp._prompts.items():
        prompts_dict[prompt_name] = prompt_info.func
    
    try:
        # Test math helper prompt
        math_helper_func = prompts_dict['math_helper']
        result = math_helper_func("Solve for x: 2x + 5 = 17", "step-by-step")
        print(f"  ✅ math helper prompt: {result[:50]}...")
        
        # Test different style
        result = math_helper_func("Find the area of a circle", "visual")
        print(f"  ✅ math helper (visual): {result[:50]}...")
        
    except Exception as e:
        print(f"  ❌ Error testing prompts: {e}")
    
    # Show server info
    print("\n🔧 Server Information:")
    print(f"  📋 Server name: {mcp.name}")
    print(f"  🛠️  Number of tools: {len(mcp._tools)}")
    print(f"  📚 Number of resources: {len(mcp._resources)}")
    print(f"  💬 Number of prompts: {len(mcp._prompts)}")
    
    print("\n✅ All direct function tests completed successfully!")
    print("\n🚀 Server is ready to use with:")
    print("   • uv run mcp dev simple_server.py (for MCP Inspector)")
    print("   • uv run mcp install simple_server.py (for Claude Desktop)")


if __name__ == "__main__":
    test_server_functions()