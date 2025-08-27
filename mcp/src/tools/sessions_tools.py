from fastmcp import Context
from dto.McpResponse import McpResponse
from openf1_client import openf1_client
from loguru import logger

def register_tools(mcp):
    """Register all sessions tools for the MCP Server"""

    @mcp.tool("get_sessions")
    async def get_sessions(
        ctx: Context,
        circuit_key: int = None,
        circuit_short_name: str = None,
        country_code: str = None,
        country_key: int = None,
        country_name: str = None,
        date_end: str = None,
        date_start: str = None,
        gmt_offset: str = None,
        location: str = None,
        meeting_key: int = None,
        session_key: int = None,
        session_name: str = None,
        session_type: str = None,
        year: int = None,
    ) -> McpResponse:
        """Use to get sessions data"""
        try:
            kwargs = locals()
            kwargs.pop("ctx")
            kwargs = {k: v for k, v in kwargs.items() if v is not None}

            logger.info(f"Getting sessions with parameters: {kwargs}")
            data = openf1_client.sessions.get_sessions(**kwargs)
            return McpResponse(message="Sessions retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving sessions: {e}")
            return McpResponse(message=f"Error retrieving sessions: {e}", data={})
