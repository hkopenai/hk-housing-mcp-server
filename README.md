# Hong Kong housing Data MCP Server

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue.svg)](https://github.com/hkopenai/hk-housing-mcp-server)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is an MCP server that provides access to housing related data in Hong Kong through a FastMCP interface.

## Features

### Private Storage Statistics
- Get completions, stock and vacancy statistics for private storage in Hong Kong

## Data Source

- Private storage statistics from Rating and Valuation Department

## Examples

* Get private storage statistics for 2020

## Setup

1. Clone this repository
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   python app.py
   ```

### Running Options

- Default stdio mode: `python app.py`
- SSE mode (port 8000): `python app.py --sse`

## Cline Integration

To connect this MCP server to Cline using stdio:

1. Add this configuration to your Cline MCP settings (cline_mcp_settings.json):
```json
{
  "hk-housing": {
    "disabled": false,
    "timeout": 3,
    "type": "stdio",
    "command": "uvx",
    "args": [
      "hkopenai.hk-housing-mcp-server"
    ]
  }
}
```

## Testing

Tests are available in the `tests/` directory. Run with:
```bash
pytest
```
