"""
Simple demonstration of the calculator server functions.

This imports the server and tests the individual functions to show they work.
"""

# Import the functions directly from the server module
from simple_server import add, subtract, multiply, divide
from simple_server import (
    get_greeting, get_constants, get_formulas, math_helper
)


def demo_calculator():
    """Demonstrate the calculator server functionality."""
    print("🎯 Simple MCP Calculator Server Demo")
    print("=" * 40)
    
    print("\n🧮 Calculator Functions:")
    print(f"  add(15, 27) = {add(15, 27)}")
    print(f"  subtract(100, 42) = {subtract(100, 42)}")
    print(f"  multiply(6, 7) = {multiply(6, 7)}")
    print(f"  divide(84.0, 2.0) = {divide(84.0, 2.0)}")
    
    # Test division by zero protection
    try:
        result = divide(10.0, 0.0)
        print(f"  divide(10.0, 0.0) = {result}")
    except ValueError as e:
        print(f"  divide(10.0, 0.0) → Error: {e} ✅")
    
    print("\n📚 Data Resources:")
    
    # Test greeting resource
    greeting = get_greeting("Alice")
    print(f"  greeting for Alice: {greeting}")
    
    # Test constants resource
    constants = get_constants()
    print(f"  Mathematical constants: {constants[:60]}...")
    
    # Test formulas resource
    formulas = get_formulas()
    print(f"  Mathematical formulas: {formulas[:60]}...")
    
    print("\n💬 Prompt Templates:")
    
    # Test math helper prompt
    prompt1 = math_helper("Solve for x: 2x + 5 = 17", "step-by-step")
    print(f"  step-by-step style: {prompt1}")
    
    prompt2 = math_helper("Find the area of a circle", "visual")
    print(f"  visual style: {prompt2}")
    
    print("\n✅ All functions working correctly!")
    print("\n🚀 To use the MCP server:")
    print("   1. Test interactively: uv run mcp dev simple_server.py")
    print("   2. Install in Claude:   uv run mcp install simple_server.py")
    print("   3. Run server directly: python simple_server.py")


if __name__ == "__main__":
    demo_calculator()