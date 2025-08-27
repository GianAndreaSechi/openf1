from fastmcp import Context
from dto.mcp_response import McpResponse
from openf1_client import openf1_client
from loguru import logger
from dto.interval_dto import IntervalDTO

def register_tools(mcp):
    """Register all intervals tools for the MCP Server"""

    @mcp.tool("get_intervals")
    async def get_intervals(ctx: Context, interval_dto: IntervalDTO) -> McpResponse:
        """Use to get intervals data"""
        try:
            kwargs = interval_dto.model_dump(exclude_unset=True)
            logger.info(f"Getting intervals with parameters: {kwargs}")
            data = openf1_client.intervals.get_intervals(**kwargs)
            return McpResponse(message="Intervals retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving intervals: {e}")
            return McpResponse(message=f"Error retrieving intervals: {e}", data={})
