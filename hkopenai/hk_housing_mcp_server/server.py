"""
Module for creating and running the HK OpenAI Housing MCP Server.

This module sets up the MCP server with tools for accessing housing data in Hong Kong,
specifically private storage information from the Rating and Valuation Department.
"""

from fastmcp import FastMCP
from .tools import private_storage


def server():
    """Create and configure the MCP server"""
    mcp = FastMCP(name="HK OpenAI housing Server")

    private_storage.register(mcp)

    return mcp
