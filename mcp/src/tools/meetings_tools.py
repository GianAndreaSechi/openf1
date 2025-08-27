from fastmcp import Context
from dto.McpResponse import McpResponse
from openf1_client import openf1_client
from loguru import logger

def register_tools(mcp):
    """Register all meetings tools for the MCP Server"""

    @mcp.tool("get_meetings")
    async def get_meetings(
        ctx: Context,
        circuit_key: int = None,
        circuit_short_name: str = None,
        country_code: str = None,
        country_key: int = None,
        country_name: str = None,
        date_start: str = None,
        gmt_offset: str = None,
        location: str = None,
        meeting_key: int = None,
        meeting_name: str = None,
        meeting_official_name: str = None,
        year: int = None,
    ) -> McpResponse:
        """Use to get meetings data"""
        try:
            kwargs = locals()
            kwargs.pop("ctx")
            kwargs = {k: v for k, v in kwargs.items() if v is not None}

            logger.info(f"Getting meetings with parameters: {kwargs}")
            data = openf1_client.meetings.get_meetings(**kwargs)
            return McpResponse(message="Meetings retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving meetings: {e}")
            return McpResponse(message=f"Error retrieving meetings: {e}", data={})
