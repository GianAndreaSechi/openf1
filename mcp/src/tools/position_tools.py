from fastmcp import Context
from dto.McpResponse import McpResponse
from openf1_client import openf1_client
from loguru import logger

def register_tools(mcp):
    """Register all position tools for the MCP Server"""

    @mcp.tool("get_position")
    async def get_position(
        ctx: Context,
        date: str = None,
        driver_number: int = None,
        meeting_key: int = None,
        position: int = None,
        session_key: int = None,
    ) -> McpResponse:
        """Use to get position data"""
        try:
            kwargs = locals()
            kwargs.pop("ctx")
            kwargs = {k: v for k, v in kwargs.items() if v is not None}

            logger.info(f"Getting position with parameters: {kwargs}")
            data = openf1_client.position.get_position(**kwargs)
            return McpResponse(message="Position retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving position: {e}")
            return McpResponse(message=f"Error retrieving position: {e}", data={})
