from fastmcp import Context
from dto.mcp_response import McpResponse
from openf1_client import openf1_client
from loguru import logger
from dto.lap_dto import LapDTO
import json

def register_tools(mcp):
    """Register all laps tools for the MCP Server"""

    @mcp.tool("get_laps")
    async def get_laps(ctx: Context, lap_dto: LapDTO) -> McpResponse:
        """Use to get laps data"""
        try:
            kwargs = lap_dto.model_dump(exclude_unset=True)
            logger.info(f"Getting laps with parameters: {kwargs}")
            data = json.loads(openf1_client.laps.get_laps(**kwargs))
            return McpResponse(message="Laps retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving laps: {e}")
            return McpResponse(message=f"Error retrieving laps: {e}", data={})
