from mcpserver.deployment import mcp
from mcp.server import serve

def main():
    mcp.run(serve)

if __name__ == "__main__":
    main()