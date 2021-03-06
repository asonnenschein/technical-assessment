"""
This type stub file was generated by pyright.
"""

from shapely.topology import Delegating

"""
Support for GEOS spatial predicates
"""

class BinaryPredicate(Delegating):
    def __call__(self, this, other, *args): ...

class UnaryPredicate(Delegating):
    def __call__(self, this): ...
