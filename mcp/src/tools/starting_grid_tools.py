from fastmcp import Context
from dto.mcp_response import McpResponse
from openf1_client import openf1_client
from loguru import logger
from dto.starting_grid_dto import StartingGridDTO


def register_tools(mcp):
    """Register all starting_grid tools for the MCP Server"""

    @mcp.tool("get_starting_grid")
    async def get_starting_grid(ctx: Context, starting_grid_dto: StartingGridDTO) -> McpResponse:
        """Use to get starting_grid data"""
        try:
            kwargs = starting_grid_dto.model_dump(exclude_unset=True)
            logger.info(f"Getting starting_grid with parameters: {kwargs}")
            results = openf1_client.starting_grid.get_starting_grid(**kwargs)
            data = [result.to_dict() for result in results]
            return McpResponse(message="Starting grid retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving starting_grid: {e}")
            return McpResponse(message=f"Error retrieving starting_grid: {e}", data={})
