from fastmcp import Context
from dto.mcp_response import McpResponse
from openf1_client import openf1_client
from loguru import logger
from dto.session_result_dto import SessionResultDTO

def register_tools(mcp):
    """Register all session_result tools for the MCP Server"""

    @mcp.tool("get_session_result")
    async def get_session_result(ctx: Context, session_result_dto: SessionResultDTO) -> McpResponse:
        """Use to get session_result data"""
        try:
            kwargs = session_result_dto.model_dump(exclude_unset=True)
            logger.info(f"Getting session_result with parameters: {kwargs}")
            data = openf1_client.session_result.get_session_result(**kwargs)
            return McpResponse(message="Session result retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving session_result: {e}")
            return McpResponse(message=f"Error retrieving session_result: {e}", data={})
