from fastmcp import Context
from dto.mcp_response import McpResponse
from openf1_client import openf1_client
from loguru import logger
from dto.weather_dto import WeatherDTO

def register_tools(mcp):
    """Register all weather tools for the MCP Server"""

    @mcp.tool("get_weather")
    async def get_weather(ctx: Context, weather_dto: WeatherDTO) -> McpResponse:
        """Use to get weather data"""
        try:
            kwargs = weather_dto.model_dump(exclude_unset=True)
            logger.info(f"Getting weather with parameters: {kwargs}")
            data = openf1_client.weather.get_weather(**kwargs)
            return McpResponse(message="Weather retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving weather: {e}")
            return McpResponse(message=f"Error retrieving weather: {e}", data={})
