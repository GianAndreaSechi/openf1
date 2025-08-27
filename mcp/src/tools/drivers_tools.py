from fastmcp import Context
from dto.McpResponse import McpResponse
from openf1_client import openf1_client
from loguru import logger

def register_tools(mcp):
    """Register all drivers tools for the MCP Server"""

    @mcp.tool("get_drivers")
    async def get_drivers(
        ctx: Context,
        broadcast_name: str = None,
        country_code: str = None,
        driver_number: int = None,
        first_name: str = None,
        full_name: str = None,
        headshot_url: str = None,
        last_name: str = None,
        meeting_key: int = None,
        name_acronym: str = None,
        session_key: int = None,
        team_colour: str = None,
        team_name: str = None,
    ) -> McpResponse:
        """Use to get drivers data"""
        try:
            kwargs = locals()
            kwargs.pop("ctx")
            kwargs = {k: v for k, v in kwargs.items() if v is not None}

            logger.info(f"Getting drivers with parameters: {kwargs}")
            data = openf1_client.drivers.get_drivers(**kwargs)
            return McpResponse(message="Drivers retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving drivers: {e}")
            return McpResponse(message=f"Error retrieving drivers: {e}", data={})
