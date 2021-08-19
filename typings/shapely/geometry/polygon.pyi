"""
This type stub file was generated by pyright.
"""

import sys
from shapely.geometry.base import BaseGeometry
from shapely.geometry.linestring import LineString, LineStringAdapter
from shapely.geometry.proxy import PolygonProxy

"""Polygons and their linear ring components
"""
if sys.version_info[0] < 3: ...

class LinearRing(LineString):
    """
    A closed one-dimensional feature comprising one or more line segments

    A LinearRing that crosses itself or touches itself at a single point is
    invalid and operations on it may fail.
    """

    def __init__(self, coordinates=...) -> None:
        """
        Parameters
        ----------
        coordinates : sequence
            A sequence of (x, y [,z]) numeric coordinate pairs or triples.
            Also can be a sequence of Point objects.

        Rings are implicitly closed. There is no need to specific a final
        coordinate pair identical to the first.

        Example
        -------
        Construct a square ring.

          >>> ring = LinearRing( ((0, 0), (0, 1), (1 ,1 ), (1 , 0)) )
          >>> ring.is_closed
          True
          >>> ring.length
          4.0
        """
        ...
    @property
    def __geo_interface__(self): ...
    _get_coords = ...
    coords = ...
    def __setstate__(self, state):  # -> None:
        """WKB doesn't differentiate between LineString and LinearRing so we
        need to move the coordinate sequence into the correct geometry type"""
        ...
    @property
    def is_ccw(self):  # -> bool:
        """True is the ring is oriented counter clock-wise"""
        ...
    @property
    def is_simple(self):  # -> bool:
        """True if the geometry is simple, meaning that any self-intersections
        are only at boundary points, else False"""
        ...

class LinearRingAdapter(LineStringAdapter):
    __p__ = ...
    def __init__(self, context) -> None: ...
    @property
    def __geo_interface__(self): ...
    coords = ...

def asLinearRing(context):  # -> LinearRingAdapter:
    """Adapt an object to the LinearRing interface"""
    ...

class InteriorRingSequence:
    _factory = ...
    _geom = ...
    __p__ = ...
    _ndim = ...
    _index = ...
    _length = ...
    __rings__ = ...
    _gtag = ...
    def __init__(self, parent) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    if sys.version_info[0] < 3: ...
    def __len__(self): ...
    def __getitem__(self, key): ...
    def gtag(self): ...

class Polygon(BaseGeometry):
    """
    A two-dimensional figure bounded by a linear ring

    A polygon has a non-zero area. It may have one or more negative-space
    "holes" which are also bounded by linear rings. If any rings cross each
    other, the feature is invalid and operations on it may fail.

    Attributes
    ----------
    exterior : LinearRing
        The ring which bounds the positive space of the polygon.
    interiors : sequence
        A sequence of rings which bound all existing holes.
    """

    _exterior = ...
    _interiors = ...
    _ndim = ...
    def __init__(self, shell=..., holes=...) -> None:
        """
        Parameters
        ----------
        shell : sequence
            A sequence of (x, y [,z]) numeric coordinate pairs or triples.
            Also can be a sequence of Point objects.
        holes : sequence
            A sequence of objects which satisfy the same requirements as the
            shell parameters above

        Example
        -------
        Create a square polygon with no holes

          >>> coords = ((0., 0.), (0., 1.), (1., 1.), (1., 0.), (0., 0.))
          >>> polygon = Polygon(coords)
          >>> polygon.area
          1.0
        """
        ...
    @property
    def exterior(self): ...
    @property
    def interiors(self): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    __hash__ = ...
    @property
    def ctypes(self): ...
    @property
    def __array_interface__(self): ...
    @property
    def coords(self): ...
    @property
    def __geo_interface__(self): ...
    def svg(self, scale_factor=..., fill_color=...):  # -> str:
        """Returns SVG path element for the Polygon geometry.

        Parameters
        ==========
        scale_factor : float
            Multiplication factor for the SVG stroke-width.  Default is 1.
        fill_color : str, optional
            Hex string for fill color. Default is to use "#66cc99" if
            geometry is valid, and "#ff3333" if invalid.
        """
        ...
    @classmethod
    def from_bounds(cls, xmin, ymin, xmax, ymax):  # -> Polygon:
        """Construct a `Polygon()` from spatial bounds."""
        ...

class PolygonAdapter(PolygonProxy, Polygon):
    def __init__(self, shell, holes=...) -> None: ...

def asPolygon(shell, holes=...):  # -> PolygonAdapter:
    """Adapt objects to the Polygon interface"""
    ...

def orient(polygon, sign=...): ...
def geos_linearring_from_py(ob, update_geom=..., update_ndim=...): ...
def update_linearring_from_py(geom, ob): ...
def geos_polygon_from_py(shell, holes=...): ...
