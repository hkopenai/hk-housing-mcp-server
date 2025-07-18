"""
Module for testing the MCP server creation and tool registration.

This module contains unit tests to verify the correct setup and behavior
of the MCP server and its associated tools.
"""

import unittest
from unittest.mock import patch, Mock
from hkopenai.hk_housing_mcp_server.server import server


class TestApp(unittest.TestCase):
    """
    Test class for verifying MCP server functionality.

    This class contains test cases to ensure the server is created correctly
    and that tools are properly registered and callable.
    """

    @patch("fastmcp.FastMCP")
    @patch("fastmcp.FastMCP")
    def test_create_mcp_server(self, mock_tool_private_storage, mock_fastmcp_class):
        # Call the function under test
        mcp_instance = server()

        # Assertions
        mock_fastmcp_class.assert_called_once_with(name="HK OpenAI housing Server")
        mock_tool_private_storage.register.assert_called_once_with(mock_fastmcp_class.return_value)
        self.assertEqual(mcp_instance, mock_fastmcp_class.return_value)


if __name__ == "__main__":
    unittest.main()