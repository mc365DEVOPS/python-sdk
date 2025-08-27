"""
Simple MCP server that exposes a calculator tool and some data.

This server demonstrates:
- Calculator tools (add, subtract, multiply, divide)
- Dynamic greeting resource
- Greeting prompt

To run with MCP Inspector:
    uv run mcp dev simple_server.py

To install in Claude Desktop:
    uv run mcp install simple_server.py
"""

from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Simple Calculator Server")


# Calculator tools
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}! Welcome to the Simple Calculator Server!"


# Add some static data resources
@mcp.resource("data://constants")
def get_constants() -> str:
    """Get mathematical constants"""
    return """Mathematical Constants:
- π (pi): 3.14159265359
- e (Euler's number): 2.71828182846
- φ (Golden ratio): 1.61803398875
- √2 (Square root of 2): 1.41421356237
"""


@mcp.resource("data://formulas")
def get_formulas() -> str:
    """Get common mathematical formulas"""
    return """Common Mathematical Formulas:
- Area of circle: π × r²
- Circumference of circle: 2 × π × r
- Pythagorean theorem: a² + b² = c²
- Quadratic formula: x = (-b ± √(b² - 4ac)) / 2a
- Area of rectangle: length × width
- Volume of sphere: (4/3) × π × r³
"""


# Add a prompt for mathematical assistance
@mcp.prompt()
def math_helper(problem: str, style: str = "step-by-step") -> str:
    """Generate a prompt for solving mathematical problems"""
    styles = {
        "step-by-step": "Please solve this math problem step by step, showing all work",
        "quick": "Please solve this math problem quickly and concisely",
        "detailed": "Please solve this math problem with detailed explanations and examples",
        "visual": "Please solve this math problem and include visual representations where helpful"
    }
    
    selected_style = styles.get(style, styles["step-by-step"])
    return f"{selected_style}: {problem}"


if __name__ == "__main__":
    # Run the server
    mcp.run()