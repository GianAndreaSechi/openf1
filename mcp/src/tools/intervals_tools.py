from fastmcp import Context
from dto.McpResponse import McpResponse
from openf1_client import openf1_client
from loguru import logger

def register_tools(mcp):
    """Register all intervals tools for the MCP Server"""

    @mcp.tool("get_intervals")
    async def get_intervals(
        ctx: Context,
        date: str = None,
        driver_number: int = None,
        gap_to_leader: float = None,
        interval: float = None,
        meeting_key: int = None,
        session_key: int = None,
    ) -> McpResponse:
        """Use to get intervals data"""
        try:
            kwargs = locals()
            kwargs.pop("ctx")
            kwargs = {k: v for k, v in kwargs.items() if v is not None}

            logger.info(f"Getting intervals with parameters: {kwargs}")
            data = openf1_client.intervals.get_intervals(**kwargs)
            return McpResponse(message="Intervals retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving intervals: {e}")
            return McpResponse(message=f"Error retrieving intervals: {e}", data={})
