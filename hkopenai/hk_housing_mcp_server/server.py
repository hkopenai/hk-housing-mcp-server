"""
Module for creating and running the HK OpenAI Housing MCP Server.

This module sets up the MCP server with tools for accessing housing data in Hong Kong,
specifically private storage information from the Rating and Valuation Department.
"""

import argparse
from fastmcp import FastMCP
from hkopenai.hk_housing_mcp_server import tool_private_storage
from typing import Dict, Annotated, Optional
from pydantic import Field


def create_mcp_server():
    """Create and configure the MCP server"""
    mcp = FastMCP(name="HK OpenAI housing Server")

    @mcp.tool(
        description="Private Storage - Completions, Stock and Vacancy in Hong Kong. Data source: Rating and Valuation Department"
    )
    def get_private_storage(
        year: Annotated[
            Optional[int], Field(description="Filter by specific year")
        ] = None,
    ) -> Dict:
        return tool_private_storage.get_private_storage(year)

    return mcp


def main():
    """
    Main function to run the MCP Server.
    
    Parses command line arguments to determine the mode of operation (SSE or stdio)
    and starts the server accordingly.
    """
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "-s", "--sse", action="store_true", help="Run in SSE mode instead of stdio"
    )
    parser.add_argument(
        "--host", type=str, default="127.0.0.1", help="Host to bind the server to"
    )
    args = parser.parse_args()

    server = create_mcp_server()

    if args.sse:
        server.run(transport="streamable-http", host=args.host)
        print(f"MCP Server running in SSE mode on port 8000, bound to {args.host}")
    else:
        server.run()
        print("MCP Server running in stdio mode")


if __name__ == "__main__":
    main()
