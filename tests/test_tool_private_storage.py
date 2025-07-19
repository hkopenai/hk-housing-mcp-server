"""
Module for testing the private storage tool functionality.

This module contains unit tests for fetching and processing private storage data.
"""

import unittest
from unittest.mock import patch, MagicMock
import pandas as pd

from hkopenai.hk_housing_mcp_server.tools.private_storage import (
    _get_private_storage,
    register,
)


class TestPrivateStorage(unittest.TestCase):
    """
    Test class for verifying private storage functionality.

    This class contains test cases to ensure the data fetching and processing
    for private storage data work as expected.
    """

    def test_get_private_storage(self):
        """
        Test the retrieval and filtering of private storage statistics.

        This test verifies that the function correctly fetches and filters data by year,
        and handles error cases.
        """
        # Mock the CSV data with structure matching actual implementation
        mock_csv_data = [
            {"Year": 2020, "Completions": 100, "Completions_Remarks": "", "Stock_at_year_end": 1000, "Stock_at_year_end_Remarks": "", "Vacancy_at_year_end": 50, "Vacancy_at_year_end_Remarks": "", "Vacancy_as_a_percent_of_stock": 5.0, "Vacancy_as_a_percent_of_stock_Remarks": ""},
            {"Year": 2021, "Completions": 110, "Completions_Remarks": "", "Stock_at_year_end": 1100, "Stock_at_year_end_Remarks": "", "Vacancy_at_year_end": 55, "Vacancy_at_year_end_Remarks": "", "Vacancy_as_a_percent_of_stock": 5.0, "Vacancy_as_a_percent_of_stock_Remarks": ""},
            {"Year": 2022, "Completions": 120, "Completions_Remarks": "", "Stock_at_year_end": 1200, "Stock_at_year_end_Remarks": "", "Vacancy_at_year_end": 60, "Vacancy_at_year_end_Remarks": "", "Vacancy_as_a_percent_of_stock": 5.0, "Vacancy_as_a_percent_of_stock_Remarks": ""}
        ]

        with patch(
            "hkopenai.hk_housing_mcp_server.tools.private_storage.fetch_csv_from_url"
        ) as mock_fetch_csv_from_url:
            # Setup mock response for successful data fetching
            mock_fetch_csv_from_url.return_value = mock_csv_data

            # Test filtering by year
            result = _get_private_storage(year=2021)
            
            self.assertEqual(len(result), 1)
            self.assertEqual(int(result[0]["Year"]), 2021)  # Convert to int since CSV returns strings
            self.assertEqual(result[0]["Stock_at_year_end"], 1100)
            self.assertEqual(result[0]["Vacancy_at_year_end"], 55)
            self.assertEqual(result[0]["Vacancy_as_a_percent_of_stock"], 5.0)

            # Test no year filter
            result = _get_private_storage()
            self.assertEqual(len(result), 3)

            # Test empty result for non-matching year
            result = _get_private_storage(year=2023)
            self.assertEqual(len(result), 0)
            
            # Test string year input
            result = _get_private_storage(year="2021")
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0]["Year"], 2021)  # Verify integer comparison works

            # Test error handling when fetch_csv_from_url returns an error
            mock_fetch_csv_from_url.return_value = {"error": "CSV fetch failed"}
            result = _get_private_storage(year=2021)
            self.assertEqual(result, {"error": "CSV fetch failed"})

            # Test empty data case
            mock_fetch_csv_from_url.return_value = []
            result = _get_private_storage(year=2021)
            self.assertEqual(result, [])

    def test_register_tool(self):
        """
        Test the registration of the get_private_storage tool.

        This test verifies that the register function correctly registers the tool
        with the FastMCP server and that the registered tool calls the underlying
        _get_private_storage function.
        """
        mock_mcp = MagicMock()

        # Call the register function
        register(mock_mcp)

        # Verify that mcp.tool was called with the correct description
        mock_mcp.tool.assert_called_once_with(
            description="Private Storage - Completions, Stock and Vacancy in Hong Kong. Data source: Rating and Valuation Department"
        )

        # Get the mock that represents the decorator returned by mcp.tool
        mock_decorator = mock_mcp.tool.return_value

        # Verify that the mock decorator was called once (i.e., the function was decorated)
        mock_decorator.assert_called_once()

        # The decorated function is the first argument of the first call to the mock_decorator
        decorated_function = mock_decorator.call_args[0][0]

        # Verify the name of the decorated function
        self.assertEqual(decorated_function.__name__, "get_private_storage")

        # Call the decorated function and verify it calls _get_private_storage
        with patch(
            "hkopenai.hk_housing_mcp_server.tools.private_storage._get_private_storage"
        ) as mock_get_private_storage:
            decorated_function(year=2021)
            mock_get_private_storage.assert_called_once_with(2021)
