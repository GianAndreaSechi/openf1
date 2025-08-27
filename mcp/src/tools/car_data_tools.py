from fastmcp import Context
from dto.McpResponse import McpResponse
from openf1_client import openf1_client
from loguru import logger

def register_tools(mcp):
    """Register all car_data tools for the MCP Server"""

    @mcp.tool("get_car_data")
    async def get_car_data(
        ctx: Context,
        brake: int = None,
        date: str = None,
        driver_number: int = None,
        drs: int = None,
        meeting_key: int = None,
        n_gear: int = None,
        rpm: int = None,
        session_key: int = None,
        speed: int = None,
        throttle: int = None,
    ) -> McpResponse:
        """Use to get car_data data"""
        try:
            kwargs = locals()
            kwargs.pop("ctx")
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            
            logger.info(f"Getting car_data with parameters: {kwargs}")
            data = openf1_client.car_data.get_car_data(**kwargs)
            return McpResponse(message="Car data retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving car_data: {e}")
            return McpResponse(message=f"Error retrieving car_data: {e}", data={})
