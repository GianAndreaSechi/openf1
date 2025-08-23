from fastmcp import Context
from loguru import logger

def register_tools(mcp):
    """Register all healthz tools for the MCP Server"""

    @mcp.tool("healthz")
    async def healthz(ctx: Context) -> dict:
        """Use to know if MCP is alive"""
        return {"ping": now()}