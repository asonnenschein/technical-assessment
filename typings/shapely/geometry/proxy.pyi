"""
This type stub file was generated by pyright.
"""

"""Proxy for coordinates stored outside Shapely geometries
"""
class CachingGeometryProxy:
    context = ...
    factory = ...
    __geom__ = ...
    _gtag = ...
    def __init__(self, context) -> None:
        ...
    
    def empty(self, val=...): # -> None:
        ...
    
    def gtag(self): # -> int:
        ...
    


class PolygonProxy(CachingGeometryProxy):
    ...

