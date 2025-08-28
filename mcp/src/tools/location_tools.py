from fastmcp import Context
from dto.mcp_response import McpResponse
from openf1_client import openf1_client
from loguru import logger
from dto.location_dto import LocationDTO


def register_tools(mcp):
    """Register all location tools for the MCP Server"""

    @mcp.tool("get_location")
    async def get_location(ctx: Context, location_dto: LocationDTO) -> McpResponse:
        """Use to get location data"""
        try:
            kwargs = location_dto.model_dump(exclude_unset=True)
            logger.info(f"Getting location with parameters: {kwargs}")
            results = openf1_client.location.get_location(**kwargs)
            data = [result.to_dict() for result in results]
            return McpResponse(message="Location retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving location: {e}")
            return McpResponse(message=f"Error retrieving location: {e}", data={})
