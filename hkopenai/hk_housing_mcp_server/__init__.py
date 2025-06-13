"""Hong Kong housing MCP Server package."""
from .app import main
from .tool_private_storage import get_private_storage

__version__ = "0.1.0"
__all__ = ['main', 'get_private_storage']
