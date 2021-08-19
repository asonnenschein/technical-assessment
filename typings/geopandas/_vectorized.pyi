"""
This type stub file was generated by pyright.
"""

from . import _compat as compat

"""
Compatibility shim for the vectorized geometry operations.

Uses PyGEOS if available/set, otherwise loops through Shapely geometries.

"""
_names = ...
if compat.USE_PYGEOS:
    type_mapping = ...
    geometry_type_ids = ...
    geometry_type_values = ...
else: ...

def from_shapely(data):  # -> ndarray[Unknown, Unknown]:
    """
    Convert a list or array of shapely objects to an object-dtype numpy
    array of validated geometry elements.

    """
    ...

def to_shapely(data): ...
def from_wkb(data):  # -> ndarray[Unknown, Unknown]:
    """
    Convert a list or array of WKB objects to a np.ndarray[geoms].
    """
    ...

def to_wkb(data, hex=..., **kwargs): ...
def from_wkt(data):  # -> ndarray[Unknown, Unknown]:
    """
    Convert a list or array of WKT objects to a np.ndarray[geoms].
    """
    ...

def to_wkt(data, **kwargs): ...
def points_from_xy(x, y, z=...): ...
def is_valid(data): ...
def is_empty(data): ...
def is_simple(data): ...
def is_ring(data): ...
def is_closed(data): ...
def has_z(data): ...
def geom_type(data): ...
def area(data): ...
def length(data): ...
def boundary(data): ...
def centroid(data): ...
def convex_hull(data): ...
def envelope(data): ...
def exterior(data): ...
def interiors(data): ...
def representative_point(data): ...
def covers(data, other): ...
def covered_by(data, other): ...
def contains(data, other): ...
def crosses(data, other): ...
def disjoint(data, other): ...
def equals(data, other): ...
def intersects(data, other): ...
def overlaps(data, other): ...
def touches(data, other): ...
def within(data, other): ...
def equals_exact(data, other, tolerance): ...
def almost_equals(self, other, decimal): ...
def difference(data, other): ...
def intersection(data, other): ...
def symmetric_difference(data, other): ...
def union(data, other): ...
def distance(data, other): ...
def buffer(data, distance, resolution=..., **kwargs): ...
def interpolate(data, distance, normalized=...): ...
def simplify(data, tolerance, preserve_topology=...): ...
def normalize(data): ...
def project(data, other, normalized=...): ...
def relate(data, other): ...
def unary_union(data): ...
def get_x(data): ...
def get_y(data): ...
def get_z(data): ...
def bounds(data): ...
def transform(data, func): ...
