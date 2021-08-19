"""
This type stub file was generated by pyright.
"""

import sys
from shapely.geometry.base import BaseGeometry
from shapely.geometry.proxy import CachingGeometryProxy

"""Line strings and related utilities
"""
if sys.version_info[0] < 3: ...

class LineString(BaseGeometry):
    """
    A one-dimensional figure comprising one or more line segments

    A LineString has non-zero length and zero area. It may approximate a curve
    and need not be straight. Unlike a LinearRing, a LineString is not closed.
    """

    def __init__(self, coordinates=...) -> None:
        """
        Parameters
        ----------
        coordinates : sequence
            A sequence of (x, y [,z]) numeric coordinate pairs or triples or
            an object that provides the numpy array interface, including
            another instance of LineString.

        Example
        -------
        Create a line with two segments

          >>> a = LineString([[0, 0], [1, 0], [1, 1]])
          >>> a.length
          2.0
        """
        ...
    @property
    def __geo_interface__(self): ...
    def svg(self, scale_factor=..., stroke_color=...):  # -> str:
        """Returns SVG polyline element for the LineString geometry.

        Parameters
        ==========
        scale_factor : float
            Multiplication factor for the SVG stroke-width.  Default is 1.
        stroke_color : str, optional
            Hex string for stroke color. Default is to use "#66cc99" if
            geometry is valid, and "#ff3333" if invalid.
        """
        ...
    @property
    def ctypes(self): ...
    def array_interface(
        self,
    ):  # -> dict[str, int | str | tuple[Literal[0]] | Array[c_double]] | Any:
        """Provide the Numpy array protocol."""
        ...
    __array_interface__ = ...
    coords = ...
    @property
    def xy(self):  # -> Any:
        """Separate arrays of X and Y coordinate values

        Example:

          >>> x, y = LineString(((0, 0), (1, 1))).xy
          >>> list(x)
          [0.0, 1.0]
          >>> list(y)
          [0.0, 1.0]
        """
        ...
    def parallel_offset(
        self, distance, side=..., resolution=..., join_style=..., mitre_limit=...
    ):  # -> BaseGeometry:
        """Returns a LineString or MultiLineString geometry at a distance from
        the object on its right or its left side.

        The side parameter may be 'left' or 'right' (default is 'right'). The
        resolution of the buffer around each vertex of the object increases by
        increasing the resolution keyword parameter or third positional
        parameter. Vertices of right hand offset lines will be ordered in
        reverse.

        The join style is for outside corners between line segments. Accepted
        values are JOIN_STYLE.round (1), JOIN_STYLE.mitre (2), and
        JOIN_STYLE.bevel (3).

        The mitre ratio limit is used for very sharp corners. It is the ratio
        of the distance from the corner to the end of the mitred offset corner.
        When two line segments meet at a sharp angle, a miter join will extend
        far beyond the original geometry. To prevent unreasonable geometry, the
        mitre limit allows controlling the maximum length of the join corner.
        Corners with a ratio which exceed the limit will be beveled.
        """
        ...

class LineStringAdapter(CachingGeometryProxy, LineString):
    def __init__(self, context) -> None: ...
    @property
    def __array_interface__(
        self,
    ):  # -> dict[str, int | str | tuple[Literal[0]] | Array[c_double]] | Any:
        """Provide the Numpy array protocol."""
        ...
    _get_coords = ...
    coords = ...

def asLineString(context):  # -> LineStringAdapter:
    """Adapt an object the LineString interface"""
    ...

def geos_linestring_from_py(ob, update_geom=..., update_ndim=...): ...
def update_linestring_from_py(geom, ob): ...
