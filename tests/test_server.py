"""
Module for testing the MCP server creation and tool registration.

This module contains unit tests to verify the correct setup and behavior
of the MCP server and its associated tools.
"""

import unittest
from unittest.mock import patch, Mock
from hkopenai.hk_housing_mcp_server.server import create_mcp_server


class TestApp(unittest.TestCase):
    """
    Test class for verifying MCP server functionality.
    
    This class contains test cases to ensure the server is created correctly
    and that tools are properly registered and callable.
    """
    @patch("hkopenai.hk_housing_mcp_server.server.FastMCP")
    @patch("hkopenai.hk_housing_mcp_server.server.tool_private_storage")
    def test_create_mcp_server(self, mock_tool_private_storage, mock_fastmcp):
        """
        Test the creation of the MCP server and tool registration.
        
        This test verifies that the server is created with the correct configuration,
        tools are registered properly, and they call the underlying functions as expected.
        """
        # Setup mocks
        mock_server = Mock()

        # Configure mock_server.tool to return a mock that acts as the decorator
        # This mock will then be called with the function to be decorated
        mock_server.tool.return_value = Mock()
        mock_fastmcp.return_value = mock_server

        # Test server creation
        server = create_mcp_server()

        # Verify server creation
        mock_fastmcp.assert_called_once()
        self.assertEqual(server, mock_server)

        mock_tool_private_storage.register.assert_called_once_with(mock_server)


if __name__ == "__main__":
    unittest.main()
