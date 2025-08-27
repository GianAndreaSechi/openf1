from fastmcp import Context
from dto.mcp_response import McpResponse
from openf1_client import openf1_client
from loguru import logger
from dto.session_dto import SessionDTO

def register_tools(mcp):
    """Register all sessions tools for the MCP Server"""

    @mcp.tool("get_sessions")
    async def get_sessions(ctx: Context, session_dto: SessionDTO) -> McpResponse:
        """Use to get sessions data"""
        try:
            kwargs = session_dto.model_dump(exclude_unset=True)
            logger.info(f"Getting sessions with parameters: {kwargs}")
            data = openf1_client.sessions.get_sessions(**kwargs)
            return McpResponse(message="Sessions retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving sessions: {e}")
            return McpResponse(message=f"Error retrieving sessions: {e}", data={})
