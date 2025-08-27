from fastmcp import Context
from dto.McpResponse import McpResponse
from openf1_client import openf1_client
from loguru import logger
from dto.race_control_dto import RaceControlDTO

def register_tools(mcp):
    """Register all race_control tools for the MCP Server"""

    @mcp.tool("get_race_control_messages")
    async def get_race_control_messages(ctx: Context, race_control_dto: RaceControlDTO) -> McpResponse:
        """Use to get race_control data"""
        try:
            kwargs = race_control_dto.model_dump(exclude_unset=True)
            logger.info(f"Getting race_control with parameters: {kwargs}")
            data = openf1_client.race_control.get_race_control_messages(**kwargs)
            return McpResponse(message="Race control retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving race_control: {e}")
            return McpResponse(message=f"Error retrieving race_control: {e}", data={})
