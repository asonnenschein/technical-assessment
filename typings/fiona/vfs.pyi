"""
This type stub file was generated by pyright.
"""

"""Implementation of Apache VFS schemes and URLs."""
SCHEMES = ...
CURLSCHEMES = ...
REMOTESCHEMES = ...

def valid_vsi(vsi):  # -> bool:
    """Ensures all parts of our vsi path are valid schemes."""
    ...

def is_remote(scheme): ...
def vsi_path(path, vsi=..., archive=...): ...
def parse_paths(
    uri, vfs=...
):  # -> tuple[Unknown | str | None, str | None, str | None]:
    """Parse a URI or Apache VFS URL into its parts

    Returns: tuple
        (path, scheme, archive)
    """
    ...
