# Make sessions directory a proper Python package
from .sessions import (
    list_all_sessions,
    close_all_sessions,
    _get_client
)

__all__ = ["list_all_sessions", "close_all_sessions", "_get_client"]
