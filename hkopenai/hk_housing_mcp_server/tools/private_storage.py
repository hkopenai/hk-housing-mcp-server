"""
Module for fetching and processing private storage data in Hong Kong.

This module provides tools to retrieve private storage statistics from the Rating
and Valuation Department (RVD) and filter the data based on specific criteria.
"""

from typing import Dict, List, Optional
from pydantic import Field
from typing_extensions import Annotated
from hkopenai_common.csv_utils import fetch_csv_from_url

def register(mcp):
    """Registers the private storage tool with the FastMCP server."""

    @mcp.tool(
        description="Private Storage - Completions, Stock and Vacancy in Hong Kong. Data source: Rating and Valuation Department"
    )
    def get_private_storage(
        year: Annotated[
            Optional[int], Field(description="Filter by specific year")
        ] = None,
    ) -> List[Dict]:
        """Get private storage statistics data with optional year filter"""
        return _get_private_storage(year)

def _get_private_storage(
    year: Annotated[Optional[int], Field(description="Filter by specific year")] = None,
) -> List[Dict]:
    """Get private storage statistics data with optional year filter"""
    data = fetch_csv_from_url("http://www.rvd.gov.hk/datagovhk/Private_Storage.csv", encoding="utf-8-sig", delimiter=",", has_title_row=True)

    if "error" in data:
        return data

    if year is not None:
        data = [row for row in data if int(row.get("Year", 0)) == int(year)]
    
    return data
