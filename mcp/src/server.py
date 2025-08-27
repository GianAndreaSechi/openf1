from fastmcp import FastMCP

from tools.healthz_tools import register_tools as register_healthz_tools
from tools.car_data_tools import register_tools as register_car_data_tools
from tools.drivers_tools import register_tools as register_drivers_tools
from tools.intervals_tools import register_tools as register_intervals_tools
from tools.laps_tools import register_tools as register_laps_tools
from tools.location_tools import register_tools as register_location_tools
from tools.meetings_tools import register_tools as register_meetings_tools
from tools.overtakes_tools import register_tools as register_overtakes_tools
from tools.pit_tools import register_tools as register_pit_tools
from tools.position_tools import register_tools as register_position_tools
from tools.race_control_tools import register_tools as register_race_control_tools
from tools.session_result_tools import register_tools as register_session_result_tools
from tools.sessions_tools import register_tools as register_sessions_tools
from tools.starting_grid_tools import register_tools as register_starting_grid_tools
from tools.stints_tools import register_tools as register_stints_tools
from tools.team_radio_tools import register_tools as register_team_radio_tools
from tools.weather_tools import register_tools as register_weather_tools

mcp = FastMCP("🏎️ Openf1 MCP Server")

register_healthz_tools(mcp)
register_car_data_tools(mcp)
register_drivers_tools(mcp)
register_intervals_tools(mcp)
register_laps_tools(mcp)
register_location_tools(mcp)
register_meetings_tools(mcp)
register_overtakes_tools(mcp)
register_pit_tools(mcp)
register_position_tools(mcp)
register_race_control_tools(mcp)
register_session_result_tools(mcp)
register_sessions_tools(mcp)
register_starting_grid_tools(mcp)
register_stints_tools(mcp)
register_team_radio_tools(mcp)
register_weather_tools(mcp)


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=80)
