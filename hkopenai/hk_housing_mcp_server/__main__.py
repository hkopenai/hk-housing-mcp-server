"""
Module serving as the entry point for the HK OpenAI Housing MCP Server.

This module imports and calls the main function from the server module to start
the MCP server application.
"""

from hkopenai.hk_housing_mcp_server.server import main

if __name__ == "__main__":
    main()
