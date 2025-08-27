from fastmcp import Context
from dto.McpResponse import McpResponse
from openf1_client import openf1_client
from loguru import logger

def register_tools(mcp):
    """Register all stints tools for the MCP Server"""

    @mcp.tool("get_stints")
    async def get_stints(
        ctx: Context,
        compound: str = None,
        driver_number: int = None,
        lap_end: int = None,
        lap_start: int = None,
        meeting_key: int = None,
        session_key: int = None,
        stint_number: int = None,
        tyre_age_at_start: int = None,
    ) -> McpResponse:
        """Use to get stints data"""
        try:
            kwargs = locals()
            kwargs.pop("ctx")
            kwargs = {k: v for k, v in kwargs.items() if v is not None}

            logger.info(f"Getting stints with parameters: {kwargs}")
            data = openf1_client.stints.get_stints(**kwargs)
            return McpResponse(message="Stints retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving stints: {e}")
            return McpResponse(message=f"Error retrieving stints: {e}", data={})
