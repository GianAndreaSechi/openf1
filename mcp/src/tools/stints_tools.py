from fastmcp import Context
from dto.McpResponse import McpResponse
from openf1_client import openf1_client
from loguru import logger
from dto.stint_dto import StintDTO

def register_tools(mcp):
    """Register all stints tools for the MCP Server"""

    @mcp.tool("get_stints")
    async def get_stints(ctx: Context, stint_dto: StintDTO) -> McpResponse:
        """Use to get stints data"""
        try:
            kwargs = stint_dto.model_dump(exclude_unset=True)
            logger.info(f"Getting stints with parameters: {kwargs}")
            data = openf1_client.stints.get_stints(**kwargs)
            return McpResponse(message="Stints retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving stints: {e}")
            return McpResponse(message=f"Error retrieving stints: {e}", data={})
