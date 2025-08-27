from fastmcp import Context
from dto.McpResponse import McpResponse
from openf1_client import openf1_client
from loguru import logger

def register_tools(mcp):
    """Register all race_control tools for the MCP Server"""

    @mcp.tool("get_race_control_messages")
    async def get_race_control_messages(
        ctx: Context,
        category: str = None,
        date: str = None,
        driver_number: int = None,
        flag: str = None,
        lap_number: int = None,
        meeting_key: int = None,
        message: str = None,
        scope: str = None,
        sector: int = None,
        session_key: int = None,
    ) -> McpResponse:
        """Use to get race_control data"""
        try:
            kwargs = locals()
            kwargs.pop("ctx")
            kwargs = {k: v for k, v in kwargs.items() if v is not None}

            logger.info(f"Getting race_control with parameters: {kwargs}")
            data = openf1_client.race_control.get_race_control_messages(**kwargs)
            return McpResponse(message="Race control retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving race_control: {e}")
            return McpResponse(message=f"Error retrieving race_control: {e}", data={})
