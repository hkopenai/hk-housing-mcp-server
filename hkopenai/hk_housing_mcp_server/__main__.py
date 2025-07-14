"""
Module serving as the entry point for the HK OpenAI Housing MCP Server.

This module imports and calls the main function from the server module to start
the MCP server application.
"""

from hkopenai_common.cli_utils import cli_main
from . import server

if __name__ == "__main__":
    cli_main(server.main, "HK Housing MCP Server")
