from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Demo")

# Add an additional tool to the server

@mcp.tool()
def add(x: int, y: int) -> int:
    """Add two numbers."""
    return x + y