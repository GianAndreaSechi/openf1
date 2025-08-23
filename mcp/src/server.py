from fastmcp import FastMCP

from tools.healthz_tools import register_tools as register_healthz_tools

mcp = FastMCP("🏎️ Openf1 MCP Server")

register_healthz_tools(mcp)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=80)