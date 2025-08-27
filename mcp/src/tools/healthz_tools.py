import time
from fastmcp import Context
from loguru import logger
from dto.mcp_response import McpResponse

def register_tools(mcp):
    """Register all healthz tools for the MCP Server"""

    @mcp.tool("healthz")
    async def healthz(ctx: Context) -> McpResponse:
        """Use to know if MCP is alive"""
        return McpResponse(message="Ping retrieved successfully", data={"ping": time.time()})