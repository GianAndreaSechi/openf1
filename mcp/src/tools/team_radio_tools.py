from fastmcp import Context
from dto.mcp_response import McpResponse
from openf1_client import openf1_client
from loguru import logger
from dto.team_radio_dto import TeamRadioDTO
import json

def register_tools(mcp):
    """Register all team_radio tools for the MCP Server"""

    @mcp.tool("get_team_radio")
    async def get_team_radio(ctx: Context, team_radio_dto: TeamRadioDTO) -> McpResponse:
        """Use to get team_radio data"""
        try:
            kwargs = team_radio_dto.model_dump(exclude_unset=True)
            logger.info(f"Getting team_radio with parameters: {kwargs}")
            data = json.loads(openf1_client.team_radio.get_team_radio(**kwargs))
            return McpResponse(message="Team radio retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving team_radio: {e}")
            return McpResponse(message=f"Error retrieving team_radio: {e}", data={})
