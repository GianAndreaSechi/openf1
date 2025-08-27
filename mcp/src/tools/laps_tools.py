from fastmcp import Context
from dto.McpResponse import McpResponse
from openf1_client import openf1_client
from loguru import logger

def register_tools(mcp):
    """Register all laps tools for the MCP Server"""

    @mcp.tool("get_laps")
    async def get_laps(
        ctx: Context,
        date_start: str = None,
        driver_number: int = None,
        duration_sector_1: float = None,
        duration_sector_2: float = None,
        duration_sector_3: float = None,
        i1_speed: int = None,
        i2_speed: int = None,
        is_pit_out_lap: bool = None,
        lap_duration: float = None,
        lap_number: int = None,
        meeting_key: int = None,
        segments_sector_1: str = None, # This is a list, but passed as a string
        segments_sector_2: str = None, # This is a list, but passed as a string
        segments_sector_3: str = None, # This is a list, but passed as a string
        session_key: int = None,
        st_speed: int = None,
    ) -> McpResponse:
        """Use to get laps data"""
        try:
            kwargs = locals()
            kwargs.pop("ctx")
            kwargs = {k: v for k, v in kwargs.items() if v is not None}

            logger.info(f"Getting laps with parameters: {kwargs}")
            data = openf1_client.laps.get_laps(**kwargs)
            return McpResponse(message="Laps retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving laps: {e}")
            return McpResponse(message=f"Error retrieving laps: {e}", data={})
