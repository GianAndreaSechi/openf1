from fastmcp import Context
from dto.mcp_response import McpResponse
from openf1_client import openf1_client
from loguru import logger
from dto.overtake_dto import OvertakeDTO


def register_tools(mcp):
    """Register all overtakes tools for the MCP Server"""

    @mcp.tool("get_overtakes")
    async def get_overtakes(ctx: Context, overtake_dto: OvertakeDTO) -> McpResponse:
        """Use to get overtakes data"""
        try:
            kwargs = overtake_dto.model_dump(exclude_unset=True)
            logger.info(f"Getting overtakes with parameters: {kwargs}")
            results = openf1_client.overtakes.get_overtakes(**kwargs)
            data = [result.to_dict() for result in results]
            return McpResponse(message="Overtakes retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving overtakes: {e}")
            return McpResponse(message=f"Error retrieving overtakes: {e}", data={})
