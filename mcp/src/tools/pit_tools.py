from fastmcp import Context
from dto.McpResponse import McpResponse
from openf1_client import openf1_client
from loguru import logger
from dto.pit_dto import PitDTO

def register_tools(mcp):
    """Register all pit tools for the MCP Server"""

    @mcp.tool("get_pit")
    async def get_pit(ctx: Context, pit_dto: PitDTO) -> McpResponse:
        """Use to get pit data"""
        try:
            kwargs = pit_dto.model_dump(exclude_unset=True)
            logger.info(f"Getting pit with parameters: {kwargs}")
            data = openf1_client.pit.get_pit(**kwargs)
            return McpResponse(message="Pit retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving pit: {e}")
            return McpResponse(message=f"Error retrieving pit: {e}", data={})
