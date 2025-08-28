from fastmcp import Context
from dto.mcp_response import McpResponse
from openf1_client import openf1_client
from loguru import logger
from dto.driver_dto import DriverDTO


def register_tools(mcp):
    """Register all drivers tools for the MCP Server"""

    @mcp.tool("get_drivers")
    async def get_drivers(ctx: Context, driver_dto: DriverDTO) -> McpResponse:
        """Use to get drivers data"""
        try:
            kwargs = driver_dto.model_dump(exclude_unset=True)
            logger.info(f"Getting drivers with parameters: {kwargs}")
            results = openf1_client.drivers.get_drivers(**kwargs)
            data = [result.to_dict() for result in results]
            return McpResponse(message="Drivers retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving drivers: {e}")
            return McpResponse(message=f"Error retrieving drivers: {e}", data={})

