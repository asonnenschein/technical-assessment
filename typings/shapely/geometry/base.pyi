"""
This type stub file was generated by pyright.
"""

import sys
from shapely.impl import delegated

"""Base geometry class and utilities

Note: a third, z, coordinate value may be used when constructing
geometry objects, but has no effect on geometric analysis. All
operations are performed in the x-y plane. Thus, geometries with
different z values may intersect or be equal.
"""
log = ...
if sys.version_info[0] < 3:
    ...
else:
    integer_types = ...
GEOMETRY_TYPES = ...
def dump_coords(geom): # -> Any | list[Unknown]:
    """Dump coordinates of a geometry in the same order as data packing"""
    ...

def geometry_type_name(g): # -> str:
    ...

def geom_factory(g, parent=...): # -> BaseGeometry:
    ...

def geom_from_wkt(data): # -> BaseGeometry:
    ...

def geom_to_wkt(ob): # -> Any:
    ...

def deserialize_wkb(data): # -> Any:
    ...

def geom_from_wkb(data): # -> BaseGeometry:
    ...

def geom_to_wkb(ob): # -> Any:
    ...

def geos_geom_from_py(ob, create_func=...): # -> tuple[Any | Unknown, Unknown]:
    """Helper function for geos_*_from_py functions in each geom type.

    If a create_func is specified the coodinate sequence is cloned and a new
    geometry is created with it, otherwise the geometry is cloned directly.
    This behaviour is useful for converting between LineString and LinearRing
    objects.
    """
    ...

def exceptNull(func): # -> (*args: Unknown, **kwargs: Unknown) -> Unknown:
    """Decorator which helps avoid GEOS operations on null pointers."""
    ...

class CAP_STYLE:
    round = ...
    flat = ...
    square = ...


class JOIN_STYLE:
    round = ...
    mitre = ...
    bevel = ...


EMPTY = ...
class BaseGeometry:
    """
    Provides GEOS spatial predicates and topological operations.

    """
    __geom__ = ...
    __p__ = ...
    _ctypes_data = ...
    _ndim = ...
    _crs = ...
    _other_owned = ...
    _is_empty = ...
    impl = ...
    _lgeos = ...
    def empty(self, val=...): # -> None:
        ...
    
    def __bool__(self): # -> bool:
        ...
    
    def __nonzero__(self): # -> bool:
        ...
    
    def __del__(self): # -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __reduce__(self): # -> tuple[Type[BaseGeometry], tuple[()], bytes]:
        ...
    
    def __setstate__(self, state): # -> None:
        ...
    
    def __and__(self, other): # -> BaseGeometry:
        ...
    
    def __or__(self, other): # -> BaseGeometry:
        ...
    
    def __sub__(self, other): # -> BaseGeometry:
        ...
    
    def __xor__(self, other): # -> BaseGeometry:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    __hash__ = ...
    @property
    def ctypes(self):
        """Return ctypes buffer"""
        ...
    
    @property
    def array_interface_base(self): # -> dict[str, int | str | Unknown]:
        ...
    
    @property
    def __array_interface__(self):
        """Provide the Numpy array protocol."""
        ...
    
    coords = ...
    @property
    def xy(self):
        """Separate arrays of X and Y coordinate values"""
        ...
    
    @property
    def __geo_interface__(self):
        """Dictionary representation of the geometry"""
        ...
    
    def geometryType(self): # -> str:
        ...
    
    @property
    def type(self): # -> str:
        ...
    
    def to_wkb(self): # -> Any:
        ...
    
    def to_wkt(self): # -> Any:
        ...
    
    @property
    def wkt(self): # -> str:
        """WKT representation of the geometry"""
        ...
    
    @property
    def wkb(self): # -> bytes:
        """WKB representation of the geometry"""
        ...
    
    @property
    def wkb_hex(self): # -> str:
        """WKB hex representation of the geometry"""
        ...
    
    def svg(self, scale_factor=..., **kwargs):
        """Raises NotImplementedError"""
        ...
    
    @property
    def geom_type(self): # -> str:
        """Name of the geometry's type, such as 'Point'"""
        ...
    
    @property
    def area(self):
        """Unitless area of the geometry (float)"""
        ...
    
    def distance(self, other):
        """Unitless distance to other geometry (float)"""
        ...
    
    def hausdorff_distance(self, other):
        """Unitless hausdorff distance to other geometry (float)"""
        ...
    
    @property
    def length(self):
        """Unitless length of the geometry (float)"""
        ...
    
    @property
    def minimum_clearance(self):
        """Unitless distance by which a node could be moved to produce an invalid geometry (float)"""
        ...
    
    @property
    def boundary(self): # -> BaseGeometry:
        """Returns a lower dimension geometry that bounds the object

        The boundary of a polygon is a line, the boundary of a line is a
        collection of points. The boundary of a point is an empty (null)
        collection.
        """
        ...
    
    @property
    def bounds(self): # -> tuple[()]:
        """Returns minimum bounding region (minx, miny, maxx, maxy)"""
        ...
    
    @property
    def centroid(self): # -> BaseGeometry:
        """Returns the geometric center of the object"""
        ...
    
    @delegated
    def representative_point(self): # -> BaseGeometry:
        """Returns a point guaranteed to be within the object, cheaply."""
        ...
    
    @property
    def convex_hull(self): # -> BaseGeometry:
        """Imagine an elastic band stretched around the geometry: that's a
        convex hull, more or less

        The convex hull of a three member multipoint, for example, is a
        triangular polygon.
        """
        ...
    
    @property
    def envelope(self): # -> BaseGeometry:
        """A figure that envelopes the geometry"""
        ...
    
    @property
    def minimum_rotated_rectangle(self): # -> BaseGeometry:
        """Returns the general minimum bounding rectangle of
        the geometry. Can possibly be rotated. If the convex hull
        of the object is a degenerate (line or point) this same degenerate
        is returned.
        """
        ...
    
    def buffer(self, distance, resolution=..., quadsegs=..., cap_style=..., join_style=..., mitre_limit=..., single_sided=...): # -> BaseGeometry:
        """Get a geometry that represents all points within a distance
        of this geometry.

        A positive distance produces a dilation, a negative distance an
        erosion. A very small or zero distance may sometimes be used to
        "tidy" a polygon.

        Parameters
        ----------
        distance : float
            The distance to buffer around the object.
        resolution : int, optional
            The resolution of the buffer around each vertex of the
            object.
        quadsegs : int, optional
            Sets the number of line segments used to approximate an
            angle fillet.  Note: the use of a `quadsegs` parameter is
            deprecated and will be gone from the next major release.
        cap_style : int, optional
            The styles of caps are: CAP_STYLE.round (1), CAP_STYLE.flat
            (2), and CAP_STYLE.square (3).
        join_style : int, optional
            The styles of joins between offset segments are:
            JOIN_STYLE.round (1), JOIN_STYLE.mitre (2), and
            JOIN_STYLE.bevel (3).
        mitre_limit : float, optional
            The mitre limit ratio is used for very sharp corners. The
            mitre ratio is the ratio of the distance from the corner to
            the end of the mitred offset corner. When two line segments
            meet at a sharp angle, a miter join will extend the original
            geometry. To prevent unreasonable geometry, the mitre limit
            allows controlling the maximum length of the join corner.
            Corners with a ratio which exceed the limit will be beveled.
        single_side : bool, optional
            The side used is determined by the sign of the buffer
            distance:

                a positive distance indicates the left-hand side
                a negative distance indicates the right-hand side

            The single-sided buffer of point geometries is the same as
            the regular buffer.  The End Cap Style for single-sided
            buffers is always ignored, and forced to the equivalent of
            CAP_FLAT.

        Returns
        -------
        Geometry

        Notes
        -----
        The return value is a strictly two-dimensional geometry. All
        Z coordinates of the original geometry will be ignored.

        Examples
        --------
        >>> from shapely.wkt import loads
        >>> g = loads('POINT (0.0 0.0)')
        >>> g.buffer(1.0).area        # 16-gon approx of a unit radius circle
        3.1365484905459389
        >>> g.buffer(1.0, 128).area   # 128-gon approximation
        3.1415138011443009
        >>> g.buffer(1.0, 3).area     # triangle approximation
        3.0
        >>> list(g.buffer(1.0, cap_style=CAP_STYLE.square).exterior.coords)
        [(1.0, 1.0), (1.0, -1.0), (-1.0, -1.0), (-1.0, 1.0), (1.0, 1.0)]
        >>> g.buffer(1.0, cap_style=CAP_STYLE.square).area
        4.0

        """
        ...
    
    @delegated
    def simplify(self, tolerance, preserve_topology=...): # -> BaseGeometry:
        """Returns a simplified geometry produced by the Douglas-Peucker
        algorithm

        Coordinates of the simplified geometry will be no more than the
        tolerance distance from the original. Unless the topology preserving
        option is used, the algorithm may produce self-intersecting or
        otherwise invalid geometries.
        """
        ...
    
    def difference(self, other): # -> BaseGeometry:
        """Returns the difference of the geometries"""
        ...
    
    def intersection(self, other): # -> BaseGeometry:
        """Returns the intersection of the geometries"""
        ...
    
    def symmetric_difference(self, other): # -> BaseGeometry:
        """Returns the symmetric difference of the geometries
        (Shapely geometry)"""
        ...
    
    def union(self, other): # -> BaseGeometry:
        """Returns the union of the geometries (Shapely geometry)"""
        ...
    
    @property
    def has_z(self): # -> bool:
        """True if the geometry's coordinate sequence(s) have z values (are
        3-dimensional)"""
        ...
    
    @property
    def is_empty(self): # -> bool:
        """True if the set of points in this geometry is empty, else False"""
        ...
    
    @property
    def is_ring(self): # -> bool:
        """True if the geometry is a closed ring, else False"""
        ...
    
    @property
    def is_closed(self): # -> bool | Any:
        """True if the geometry is closed, else False

        Applicable only to 1-D geometries."""
        ...
    
    @property
    def is_simple(self): # -> bool:
        """True if the geometry is simple, meaning that any self-intersections
        are only at boundary points, else False"""
        ...
    
    @property
    def is_valid(self): # -> bool:
        """True if the geometry is valid (definition depends on sub-class),
        else False"""
        ...
    
    def relate(self, other):
        """Returns the DE-9IM intersection matrix for the two geometries
        (string)"""
        ...
    
    def covers(self, other): # -> bool:
        """Returns True if the geometry covers the other, else False"""
        ...
    
    def contains(self, other): # -> bool:
        """Returns True if the geometry contains the other, else False"""
        ...
    
    def crosses(self, other): # -> bool:
        """Returns True if the geometries cross, else False"""
        ...
    
    def disjoint(self, other): # -> bool:
        """Returns True if geometries are disjoint, else False"""
        ...
    
    def equals(self, other): # -> bool:
        """Returns True if geometries are equal, else False

        Refers to point-set equality (or topological equality), and is equivalent to
        (self.within(other) & self.contains(other))
        """
        ...
    
    def intersects(self, other): # -> bool:
        """Returns True if geometries intersect, else False"""
        ...
    
    def overlaps(self, other): # -> bool:
        """Returns True if geometries overlap, else False"""
        ...
    
    def touches(self, other): # -> bool:
        """Returns True if geometries touch, else False"""
        ...
    
    def within(self, other): # -> bool:
        """Returns True if geometry is within the other, else False"""
        ...
    
    def equals_exact(self, other, tolerance): # -> bool:
        """Returns True if geometries are equal to within a specified
        tolerance

        Refers to coordinate equality, which requires coordinates to be equal
        and in the same order for all components of a geometry
        """
        ...
    
    def almost_equals(self, other, decimal=...): # -> bool:
        """Returns True if geometries are equal at all coordinates to a
        specified decimal place

        Refers to approximate coordinate equality, which requires coordinates be
        approximately equal and in the same order for all components of a geometry.
        """
        ...
    
    def relate_pattern(self, other, pattern): # -> bool:
        """Returns True if the DE-9IM string code for the relationship between
        the geometries satisfies the pattern, else False"""
        ...
    
    @delegated
    def project(self, other, normalized=...):
        """Returns the distance along this geometry to a point nearest the
        specified point

        If the normalized arg is True, return the distance normalized to the
        length of the linear geometry.
        """
        ...
    
    @delegated
    @exceptNull
    def interpolate(self, distance, normalized=...): # -> BaseGeometry:
        """Return a point at the specified distance along a linear geometry

        Negative length values are taken as measured in the reverse
        direction from the end of the geometry. Out-of-range index
        values are handled by clamping them to the valid range of values.
        If the normalized arg is True, the distance will be interpreted as a
        fraction of the geometry's length.
        """
        ...
    


class BaseMultipartGeometry(BaseGeometry):
    def shape_factory(self, *args):
        ...
    
    @property
    def ctypes(self):
        ...
    
    @property
    def __array_interface__(self):
        """Provide the Numpy array protocol."""
        ...
    
    @property
    def coords(self):
        ...
    
    @property
    def geoms(self): # -> GeometrySequence | list[Unknown]:
        ...
    
    def __bool__(self): # -> bool:
        ...
    
    def __iter__(self): # -> Iterator[Unknown] | Iterator[Any]:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def __getitem__(self, index): # -> Any:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    __hash__ = ...
    def svg(self, scale_factor=..., color=...): # -> str:
        """Returns a group of SVG elements for the multipart geometry.

        Parameters
        ==========
        scale_factor : float
            Multiplication factor for the SVG stroke-width.  Default is 1.
        color : str, optional
            Hex string for stroke or fill color. Default is to use "#66cc99"
            if geometry is valid, and "#ff3333" if invalid.
        """
        ...
    


class GeometrySequence:
    """
    Iterative access to members of a homogeneous multipart geometry.
    """
    shape_factory = ...
    _geom = ...
    __p__ = ...
    _ndim = ...
    def __init__(self, parent, type) -> None:
        ...
    
    def __iter__(self): # -> Generator[Unknown, None, None]:
        ...
    
    def __len__(self): # -> Any:
        ...
    
    def __getitem__(self, key): # -> Any:
        ...
    


class HeterogeneousGeometrySequence(GeometrySequence):
    """
    Iterative access to a heterogeneous sequence of geometries.
    """
    def __init__(self, parent) -> None:
        ...
    


class EmptyGeometry(BaseGeometry):
    def __init__(self) -> None:
        """Create an empty geometry."""
        ...
    


if __name__ == "__main__":
    ...