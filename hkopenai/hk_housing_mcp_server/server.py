"""
Module for creating and running the HK OpenAI Housing MCP Server.

This module sets up the MCP server with tools for accessing housing data in Hong Kong,
specifically private storage information from the Rating and Valuation Department.
"""

from fastmcp import FastMCP
from hkopenai.hk_housing_mcp_server import tool_private_storage
from typing import Dict, Annotated, Optional
from pydantic import Field


def create_mcp_server():
    """Create and configure the MCP server"""
    mcp = FastMCP(name="HK OpenAI housing Server")

    tool_private_storage.register(mcp)

    return mcp


def main(host: str, port: int, sse: bool):
    """
    Main function to run the MCP Server.
    
    Args:
        args: Command line arguments passed to the function.
    """
    server = create_mcp_server()

    if sse:
        server.run(transport="streamable-http", host=host, port=port)
        print(f"MCP Server running in SSE mode on port {args.port}, bound to {args.host}")
    else:
        server.run()
        print("MCP Server running in stdio mode")


if __name__ == "__main__":
    main()
