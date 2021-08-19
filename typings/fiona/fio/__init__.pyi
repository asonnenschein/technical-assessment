"""
This type stub file was generated by pyright.
"""

from functools import wraps

"""Fiona's command line interface"""
def with_context_env(f): # -> (*args: Unknown, **kwds: Unknown) -> Unknown:
    """Pops the Fiona Env from the passed context and executes the
    wrapped func in the context of that obj.

    Click's pass_context decorator must precede this decorator, or else
    there will be no context in the wrapper args.
    """
    ...

