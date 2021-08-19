"""
This type stub file was generated by pyright.
"""

class Require:
    """A prerequisite to building or installing a distribution"""

    def __init__(
        self, name, requested_version, module, homepage=..., attribute=..., format=...
    ) -> None: ...
    def full_name(self):  # -> str:
        """Return full package/distribution name, w/version"""
        ...
    def version_ok(self, version):  # -> bool:
        """Is 'version' sufficiently up-to-date?"""
        ...
    def get_version(self, paths=..., default=...):  # -> Any | None:
        """Get version number of installed module, 'None', or 'default'

        Search 'paths' for module.  If not found, return 'None'.  If found,
        return the extracted version attribute, or 'default' if no version
        attribute was specified, or the value cannot be determined without
        importing the module.  The version is formatted according to the
        requirement's version format (if any), unless it is 'None' or the
        supplied 'default'.
        """
        ...
    def is_present(self, paths=...):  # -> bool:
        """Return true if dependency is present on 'paths'"""
        ...
    def is_current(self, paths=...):  # -> bool:
        """Return true if dependency is present and up-to-date on 'paths'"""
        ...

def maybe_close(f): ...
def get_module_constant(module, symbol, default=..., paths=...):  # -> Any | None:
    """Find 'module' by searching 'paths', and extract 'symbol'

    Return 'None' if 'module' does not exist on 'paths', or it does not define
    'symbol'.  If the module defines 'symbol' as a constant, return the
    constant.  Otherwise, return 'default'."""
    ...

def extract_constant(code, symbol, default=...):  # -> None:
    """Extract the constant value of 'symbol' from 'code'

    If the name 'symbol' is bound to a constant value by the Python code
    object 'code', return that value.  If 'symbol' is bound to an expression,
    return 'default'.  Otherwise, return 'None'.

    Return value is based on the first assignment to 'symbol'.  'symbol' must
    be a global, or at least a non-"fast" local in the code block.  That is,
    only 'STORE_NAME' and 'STORE_GLOBAL' opcodes are checked, and 'symbol'
    must be present in 'code.co_names'.
    """
    ...
