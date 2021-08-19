"""
This type stub file was generated by pyright.
"""

import logging

"""Logging helper classes."""
class FieldSkipLogFilter(logging.Filter):
    """Filter field skip log messges.

    At most, one message per field skipped per loop will be passed.
    """
    def __init__(self, name=...) -> None:
        ...
    
    def filter(self, record): # -> bool | Literal[1]:
        """Pass record if not seen."""
        ...
    


class LogFiltering:
    def __init__(self, logger, filter) -> None:
        ...
    
    def __enter__(self): # -> None:
        ...
    
    def __exit__(self, *args, **kwargs): # -> None:
        ...
    


