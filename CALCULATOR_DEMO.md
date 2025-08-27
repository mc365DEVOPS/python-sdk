# Simple MCP Calculator Server

This is a simple MCP server that demonstrates the key features described in the README.md.

## Features

The server implements:

### Tools (Calculator Functions)
- `add(a, b)` - Add two numbers
- `subtract(a, b)` - Subtract two numbers  
- `multiply(a, b)` - Multiply two numbers
- `divide(a, b)` - Divide two numbers (with zero-division protection)

### Resources (Data Access)
- `greeting://{name}` - Dynamic personalized greetings
- `data://constants` - Mathematical constants (π, e, φ, √2)
- `data://formulas` - Common mathematical formulas

### Prompts (Interaction Templates)
- `math_helper(problem, style)` - Generate prompts for solving math problems
  - Styles: "step-by-step", "quick", "detailed", "visual"

## How to Run

### 1. Development Mode (MCP Inspector)
```bash
uv run mcp dev simple_server.py
```
This opens a web interface where you can test all tools, resources, and prompts interactively.

### 2. Claude Desktop Integration

#### Option A: Automatic Installation (Recommended)
```bash
uv run mcp install simple_server.py --name "Simple Calculator Server"
```
This automatically configures Claude Desktop to use your MCP server.

#### Option B: Manual Configuration
If the automatic installation doesn't work, you can manually configure Claude Desktop:

1. **Locate Claude Desktop Config File**:
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Linux**: `~/.config/Claude/claude_desktop_config.json`

2. **Create or Edit the Configuration File**:
   Add the following configuration to the `mcpServers` section:

   ```json
   {
     "mcpServers": {
       "simple-calculator": {
         "command": "uv",
         "args": [
           "run",
           "--directory",
           "C:\\Users\\TerryPatterson\\OneDrive - Managed Connections, LTD\\Documents\\source\\repos\\python-sdk",
           "python",
           "simple_server.py"
         ]
       }
     }
   }
   ```

   **Note**: Replace the path in `--directory` with your actual project path.

3. **Complete Configuration Example**:
   ```json
   {
     "mcpServers": {
       "simple-calculator": {
         "command": "uv",
         "args": [
           "run",
           "--directory",
           "C:\\Users\\TerryPatterson\\OneDrive - Managed Connections, LTD\\Documents\\source\\repos\\python-sdk",
           "python",
           "simple_server.py"
         ]
       }
     },
     "globalShortcut": "Ctrl+;"
   }
   ```

4. **Restart Claude Desktop**: Close and reopen Claude Desktop to load the new configuration.

5. **Verify Connection**: Look for the 🔌 plug icon in Claude Desktop, which indicates MCP servers are connected.

#### Troubleshooting Claude Desktop Connection

If you encounter issues:

- **Check the config file path**: Make sure the JSON file is in the correct location
- **Validate JSON syntax**: Use a JSON validator to ensure proper formatting
- **Verify file paths**: Ensure the `--directory` path points to your project folder
- **Check Claude Desktop logs**: Look for MCP connection errors in the app
- **Test server standalone**: Run `python simple_server.py` to verify the server works
- **Use absolute paths**: Avoid relative paths in the configuration

### 3. Direct Execution
```bash
python simple_server.py
```
This runs the server in stdio mode for programmatic access.

## Example Usage

Once connected to Claude Desktop, you can interact with the calculator server in natural language:

### Calculator Operations
- **"Add 15 and 27"** → Uses the `add` tool → Returns 42
- **"What's 100 minus 42?"** → Uses the `subtract` tool → Returns 58
- **"Multiply 6 by 7"** → Uses the `multiply` tool → Returns 42
- **"Divide 84 by 2"** → Uses the `divide` tool → Returns 42.0

### Accessing Data Resources
- **"Show me mathematical constants"** → Reads `data://constants` resource → Returns π, e, φ, √2 values
- **"What are some common formulas?"** → Reads `data://formulas` resource → Returns area, circumference, Pythagorean theorem, etc.
- **"Give me a greeting for Alice"** → Reads `greeting://Alice` resource → Returns personalized welcome message

### Using Math Assistance Prompts
- **"Help me solve 2x + 5 = 17 step by step"** → Uses `math_helper` prompt with step-by-step style
- **"I need help finding the area of a circle with visual explanations"** → Uses `math_helper` prompt with visual style

### Verification in Claude Desktop

After connecting, you should see:
1. **🔌 Plug icon** in the Claude Desktop interface indicating MCP servers are connected
2. **Access to calculator functions** when you ask math questions
3. **Automatic resource loading** when you request mathematical information
4. **Enhanced problem-solving** with the math helper prompts

### Sample Conversation

```
You: "Add 25 and 17, then multiply the result by 3"

Claude: I'll help you with that calculation using the calculator tools.

First, let me add 25 and 17:
[Uses add tool: 25 + 17 = 42]

Now I'll multiply that result by 3:
[Uses multiply tool: 42 × 3 = 126]

The final answer is 126.
```

## Code Structure

The server follows the FastMCP pattern from the README:

1. **Server Creation**: `mcp = FastMCP("Simple Calculator Server")`
2. **Tool Decoration**: `@mcp.tool()` for calculator functions
3. **Resource Decoration**: `@mcp.resource("uri://template")` for data access
4. **Prompt Decoration**: `@mcp.prompt()` for interaction templates
5. **Execution**: `mcp.run()` to start the server

This demonstrates all the core MCP concepts in a practical, working example.