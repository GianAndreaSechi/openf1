from fastmcp import Context
from dto.McpResponse import McpResponse
from openf1_client import openf1_client
from loguru import logger

def register_tools(mcp):
    """Register all weather tools for the MCP Server"""

    @mcp.tool("get_weather")
    async def get_weather(
        ctx: Context,
        air_temperature: float = None,
        date: str = None,
        humidity: int = None,
        meeting_key: int = None,
        pressure: float = None,
        rainfall: int = None,
        session_key: int = None,
        track_temperature: float = None,
        wind_direction: int = None,
        wind_speed: float = None,
    ) -> McpResponse:
        """Use to get weather data"""
        try:
            kwargs = locals()
            kwargs.pop("ctx")
            kwargs = {k: v for k, v in kwargs.items() if v is not None}

            logger.info(f"Getting weather with parameters: {kwargs}")
            data = openf1_client.weather.get_weather(**kwargs)
            return McpResponse(message="Weather retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving weather: {e}")
            return McpResponse(message=f"Error retrieving weather: {e}", data={})
