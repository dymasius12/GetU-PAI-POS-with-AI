"""Agent configuration for the MCP toolbox backed by Cloud SQL Postgres."""

from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient

# Point the toolbox client at your MCP server (ensure it is running).
toolbox = ToolboxSyncClient("http://127.0.0.1:5000")

# Load all POS tools defined in tools.yaml.
tools = toolbox.load_toolset("coffee_pos_toolset")

# Root agent configured for GetU.Coffee POS data.
root_agent = Agent(
    name="coffee_pos_agent",
    model="gemini-2.5-flash",
    description="Answer questions about GetU.Coffee sales, menus, and inventory using Cloud SQL data.",
    instruction=(
        "You are a helpful assistant for the GetU.Coffee POS. "
        "Use the provided tools to answer questions about sales, top items, categories, busy hours, "
        "inventory levels, ingredient usage, and recent orders. "
        "Prefer concise, actionable answers grounded in the database results."
    ),
    tools=tools,
)
