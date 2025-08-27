from fastmcp import Context
from dto.McpResponse import McpResponse
from openf1_client import openf1_client
from loguru import logger

def register_tools(mcp):
    """Register all location tools for the MCP Server"""

    @mcp.tool("get_location")
    async def get_location(
        ctx: Context,
        date: str = None,
        driver_number: int = None,
        meeting_key: int = None,
        session_key: int = None,
        x: int = None,
        y: int = None,
        z: int = None,
    ) -> McpResponse:
        """Use to get location data"""
        try:
            kwargs = locals()
            kwargs.pop("ctx")
            kwargs = {k: v for k, v in kwargs.items() if v is not None}

            logger.info(f"Getting location with parameters: {kwargs}")
            data = openf1_client.location.get_location(**kwargs)
            return McpResponse(message="Location retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving location: {e}")
            return McpResponse(message=f"Error retrieving location: {e}", data={})
