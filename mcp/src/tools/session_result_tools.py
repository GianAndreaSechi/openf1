from fastmcp import Context
from dto.McpResponse import McpResponse
from openf1_client import openf1_client
from loguru import logger

def register_tools(mcp):
    """Register all session_result tools for the MCP Server"""

    @mcp.tool("get_session_result")
    async def get_session_result(
        ctx: Context,
        dnf: bool = None,
        dns: bool = None,
        dsq: bool = None,
        driver_number: int = None,
        duration: float = None,
        gap_to_leader: float = None,
        number_of_laps: int = None,
        meeting_key: int = None,
        position: int = None,
        session_key: int = None,
    ) -> McpResponse:
        """Use to get session_result data"""
        try:
            kwargs = locals()
            kwargs.pop("ctx")
            kwargs = {k: v for k, v in kwargs.items() if v is not None}

            logger.info(f"Getting session_result with parameters: {kwargs}")
            data = openf1_client.session_result.get_session_result(**kwargs)
            return McpResponse(message="Session result retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving session_result: {e}")
            return McpResponse(message=f"Error retrieving session_result: {e}", data={})
