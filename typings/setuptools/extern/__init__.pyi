"""
This type stub file was generated by pyright.
"""

import importlib.util
import sys

class VendorImporter:
    """
    A PEP 302 meta path importer for finding optionally-vendored
    or otherwise naturally-installed packages from root_name.
    """

    def __init__(self, root_name, vendored_names=..., vendor_pkg=...) -> None: ...
    @property
    def search_path(self):  # -> Generator[Unknown | Literal[''], None, None]:
        """
        Search first the vendor package then as a natural package.
        """
        ...
    def load_module(self, fullname):  # -> ModuleType:
        """
        Iterate over the search path to locate and load fullname.
        """
        ...
    def create_module(self, spec): ...
    def exec_module(self, module): ...
    def find_spec(self, fullname, path=..., target=...):  # -> ModuleSpec | None:
        """Return a module spec for vendored names."""
        ...
    def install(self):  # -> None:
        """
        Install this importer into sys.meta_path if not already present.
        """
        ...

names = ...
