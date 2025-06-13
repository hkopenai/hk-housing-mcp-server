import io
import pandas as pd
import requests
from typing import Dict, List, Optional
from pydantic import Field
from typing_extensions import Annotated

def fetch_private_storage_data() -> pd.DataFrame:
    """Fetch private storage statistics data from RVD"""
    url = "http://www.rvd.gov.hk/datagovhk/Private_Storage.csv"
    response = requests.get(url)
    response.encoding = 'utf-8-sig'  # Handle BOM if present
    df = pd.read_csv(io.StringIO(response.text), skiprows=1)
    return df

def get_private_storage(
    year: Annotated[Optional[int], Field(description="Filter by specific year")] = None
) -> List[Dict]:
    """Get private storage statistics data with optional year filter"""
    df = fetch_private_storage_data()
    
    # Apply filter if provided
    if year is not None:
        df = df[df['Year'] == year]
    
    # Convert to list of dicts
    return df.to_dict('records')
