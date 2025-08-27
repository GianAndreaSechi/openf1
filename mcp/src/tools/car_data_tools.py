from fastmcp import Context
from dto.mcp_response import McpResponse
from openf1_client import openf1_client
from loguru import logger
from dto.car_data_dto import CarDataDTO

def register_tools(mcp):
    """Register all car_data tools for the MCP Server"""

    @mcp.tool("get_car_data")
    async def get_car_data(ctx: Context, car_data_dto: CarDataDTO) -> McpResponse:
        """Use to get car_data data"""
        try:
            kwargs = car_data_dto.model_dump(exclude_unset=True)
            logger.info(f"Getting car_data with parameters: {kwargs}")
            data = openf1_client.car_data.get_car_data(**kwargs)
            return McpResponse(message="Car data retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving car_data: {e}")
            return McpResponse(message=f"Error retrieving car_data: {e}", data={})
