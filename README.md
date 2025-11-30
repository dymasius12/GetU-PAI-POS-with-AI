# GetU-PAI-POS-with-AI

Configurations for exploring the GetU.Coffee point-of-sale data with Gemini and the Google Cloud ADK. The repo wires an MCP toolbox backed by Cloud SQL Postgres to a Gemini agent that can answer sales, menu, and inventory questions.

## Layout
- `mcp-toolbox/tools.yaml` — active MCP toolbox pointing at the Cloud SQL Postgres instance with POS queries (menus, orders, inventory, category mix, peak hours, etc.).
- `mcp-toolbox/retired_tools.yaml` — previous toolbox example (hotel search); kept for reference.
- `my-agents/coffee_pos_agent_app/agent.py` — Gemini 2.5 Flash agent that loads the `coffee_pos_toolset` from the toolbox server at `http://127.0.0.1:5000`.
- `my-gemini-cli-project/.gemini/settings.json` — Gemini CLI configuration that targets the same MCP server.

## Getting Started
1. Set up Python (3.10+ recommended) and install the Google Cloud ADK and MCP toolbox packages in a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install google-adk mcp-toolbox
   ```
2. Launch the MCP toolbox server against the POS tool definitions:
   ```bash
   mcp-toolbox serve mcp-toolbox/tools.yaml --host 127.0.0.1 --port 5000
   ```
3. Use the agent in your own runner or notebooks by importing the ready-made `root_agent`:
   ```python
   from coffee_pos_agent_app.agent import root_agent
   # root_agent is configured to call the toolbox server above and use Gemini 2.5 Flash
   ```
4. If you use the Gemini CLI, run it from `my-gemini-cli-project` so it picks up `.gemini/settings.json` and connects to the MCP server:
   ```bash
   cd my-gemini-cli-project
   gemini chat
   ```

## Notes
- The `tools.yaml` file currently stores database credentials in plain text. Replace them with environment-based secrets before deploying anywhere outside local testing.
- Update `my-agents/coffee_pos_agent_app/agent.py` if you move the toolbox server or want to switch models.
- Retired tools in `retired_tools.yaml` are not served by default; they remain as examples of other Postgres-backed toolsets.
