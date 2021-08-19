"""
This type stub file was generated by pyright.
"""

import contextlib

PANDAS_GE_025 = ...
PANDAS_GE_10 = ...
PANDAS_GE_11 = ...
PANDAS_GE_115 = ...
PANDAS_GE_12 = ...
SHAPELY_GE_17 = ...
SHAPELY_GE_18 = ...
SHAPELY_GE_20 = ...
GEOS_GE_390 = ...
HAS_PYGEOS = ...
USE_PYGEOS = ...
PYGEOS_SHAPELY_COMPAT = ...
PYGEOS_GE_09 = ...
def set_use_pygeos(val=...): # -> None:
    """
    Set the global configuration on whether to use PyGEOS or not.

    The default is use PyGEOS if it is installed. This can be overridden
    with an environment variable USE_PYGEOS (this is only checked at
    first import, cannot be changed during interactive session).

    Alternatively, pass a value here to force a True/False value.
    """
    ...

if shapely_warning is not None and not SHAPELY_GE_20:
    @contextlib.contextmanager
    def ignore_shapely2_warnings(): # -> Generator[None, None, None]:
        ...
    
else:
    @contextlib.contextmanager
    def ignore_shapely2_warnings(): # -> Generator[None, None, None]:
        ...
    
def import_optional_dependency(name: str, extra: str = ...): # -> ModuleType:
    """
    Import an optional dependency.

    Adapted from pandas.compat._optional::import_optional_dependency

    Raises a formatted ImportError if the module is not present.

    Parameters
    ----------
    name : str
        The module name.
    extra : str
        Additional text to include in the ImportError message.
    Returns
    -------
    module
    """
    ...

HAS_RTREE = ...
RTREE_GE_094 = ...
PYPROJ_LT_3 = ...
