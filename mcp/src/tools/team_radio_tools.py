from fastmcp import Context
from dto.McpResponse import McpResponse
from openf1_client import openf1_client
from loguru import logger

def register_tools(mcp):
    """Register all team_radio tools for the MCP Server"""

    @mcp.tool("get_team_radio")
    async def get_team_radio(
        ctx: Context,
        date: str = None,
        driver_number: int = None,
        meeting_key: int = None,
        recording_url: str = None,
        session_key: int = None,
    ) -> McpResponse:
        """Use to get team_radio data"""
        try:
            kwargs = locals()
            kwargs.pop("ctx")
            kwargs = {k: v for k, v in kwargs.items() if v is not None}

            logger.info(f"Getting team_radio with parameters: {kwargs}")
            data = openf1_client.team_radio.get_team_radio(**kwargs)
            return McpResponse(message="Team radio retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving team_radio: {e}")
            return McpResponse(message=f"Error retrieving team_radio: {e}", data={})
