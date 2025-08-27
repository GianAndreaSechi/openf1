from fastmcp import Context
from dto.McpResponse import McpResponse
from openf1_client import openf1_client
from loguru import logger

def register_tools(mcp):
    """Register all overtakes tools for the MCP Server"""

    @mcp.tool("get_overtakes")
    async def get_overtakes(
        ctx: Context,
        date: str = None,
        meeting_key: int = None,
        overtaken_driver_number: int = None,
        overtaking_driver_number: int = None,
        position: int = None,
        session_key: int = None,
    ) -> McpResponse:
        """Use to get overtakes data"""
        try:
            kwargs = locals()
            kwargs.pop("ctx")
            kwargs = {k: v for k, v in kwargs.items() if v is not None}

            logger.info(f"Getting overtakes with parameters: {kwargs}")
            data = openf1_client.overtakes.get_overtakes(**kwargs)
            return McpResponse(message="Overtakes retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving overtakes: {e}")
            return McpResponse(message=f"Error retrieving overtakes: {e}", data={})
