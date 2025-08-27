from fastmcp import Context
from dto.McpResponse import McpResponse
from openf1_client import openf1_client
from loguru import logger

def register_tools(mcp):
    """Register all starting_grid tools for the MCP Server"""

    @mcp.tool("get_starting_grid")
    async def get_starting_grid(
        ctx: Context,
        driver_number: int = None,
        lap_duration: float = None,
        meeting_key: int = None,
        position: int = None,
        session_key: int = None,
    ) -> McpResponse:
        """Use to get starting_grid data"""
        try:
            kwargs = locals()
            kwargs.pop("ctx")
            kwargs = {k: v for k, v in kwargs.items() if v is not None}

            logger.info(f"Getting starting_grid with parameters: {kwargs}")
            data = openf1_client.starting_grid.get_starting_grid(**kwargs)
            return McpResponse(message="Starting grid retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving starting_grid: {e}")
            return McpResponse(message=f"Error retrieving starting_grid: {e}", data={})
