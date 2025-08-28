from fastmcp import Context
from dto.mcp_response import McpResponse
from openf1_client import openf1_client
from loguru import logger
from dto.meeting_dto import MeetingDTO


def register_tools(mcp):
    """Register all meetings tools for the MCP Server"""

    @mcp.tool("get_meetings")
    async def get_meetings(ctx: Context, meeting_dto: MeetingDTO) -> McpResponse:
        """Use to get meetings data"""
        try:
            kwargs = meeting_dto.model_dump(exclude_unset=True)
            logger.info(f"Getting meetings with parameters: {kwargs}")
            results = openf1_client.meetings.get_meetings(**kwargs)
            data = [result.to_dict() for result in results]
            return McpResponse(message="Meetings retrieved successfully", data=data)
        except Exception as e:
            logger.error(f"Error retrieving meetings: {e}")
            return McpResponse(message=f"Error retrieving meetings: {e}", data={})
