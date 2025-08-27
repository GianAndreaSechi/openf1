from fastmcp import Context
from dto.McpResponse import McpResponse
from openf1_client import openf1_client
from loguru import logger

def register_tools(mcp):
    """Register all pit tools for the MCP Server"""

    @mcp.tool("get_pit")
    async def get_pit(
        ctx: Context,
        date: str = None,
        driver_number: int = None,
        lap_number: int = None,
        meeting_key: int = None,
        pit_duration: float = None,
        session_key: int = None,
    ) -> McpResponse:
        """Use to get pit data"""
        try:
            kwargs = locals()
            kwargs.pop("ctx")
            kwargs = {k: v for k, v in kwargs.items() if v is not None}

            logger.info(f"Getting pit with parameters: {kwargs}")
            data = openf1_client.pit.get_pit(**kwargs)
            return McpResponse(message="Pit retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving pit: {e}")
            return McpResponse(message=f"Error retrieving pit: {e}", data={})
