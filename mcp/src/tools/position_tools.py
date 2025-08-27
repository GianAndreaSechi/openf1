from fastmcp import Context
from dto.mcp_response import McpResponse
from openf1_client import openf1_client
from loguru import logger
from dto.position_dto import PositionDTO

def register_tools(mcp):
    """Register all position tools for the MCP Server"""

    @mcp.tool("get_position")
    async def get_position(ctx: Context, position_dto: PositionDTO) -> McpResponse:
        """Use to get position data"""
        try:
            kwargs = position_dto.model_dump(exclude_unset=True)
            logger.info(f"Getting position with parameters: {kwargs}")
            data = openf1_client.position.get_position(**kwargs)
            return McpResponse(message="Position retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving position: {e}")
            return McpResponse(message=f"Error retrieving position: {e}", data={})
