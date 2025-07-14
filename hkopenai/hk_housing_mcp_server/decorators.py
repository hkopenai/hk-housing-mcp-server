"""
Module for creating decorators used in the HK Housing MCP Server.

This module provides utilities for creating decorators that can be used to
register tools and other functionalities within the MCP server framework.
"""


def create_tool_registry():
    """Create a tool registry decorator that tracks decorated functions by name.

    Returns:
        A decorator function that can be used to register tools and provides
        a get(name) method to lookup registered tools by function name.
    """
    registry = {}

    def tool_decorator(description=None):
        def decorator(f):
            registry[f.__name__] = f
            return f

        return decorator

    # Add lookup capability to the decorator
    tool_decorator.get = registry.get
    return tool_decorator
