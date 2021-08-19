"""
This type stub file was generated by pyright.
"""

import pandas as pd
from pandas import Series
from geopandas.base import GeoPandasBase

_SERIES_WARNING_MSG = ...
def inherit_doc(cls): # -> (decorated: Unknown) -> Unknown:
    """
    A decorator adding a docstring from an existing method.
    """
    ...

class GeoSeries(GeoPandasBase, Series):
    """
    A Series object designed to store shapely geometry objects.

    Parameters
    ----------
    data : array-like, dict, scalar value
        The geometries to store in the GeoSeries.
    index : array-like or Index
        The index for the GeoSeries.
    crs : value (optional)
        Coordinate Reference System of the geometry objects. Can be anything accepted by
        :meth:`pyproj.CRS.from_user_input() <pyproj.crs.CRS.from_user_input>`,
        such as an authority string (eg "EPSG:4326") or a WKT string.

    kwargs
        Additional arguments passed to the Series constructor,
         e.g. ``name``.

    Examples
    --------

    >>> from shapely.geometry import Point
    >>> s = geopandas.GeoSeries([Point(1, 1), Point(2, 2), Point(3, 3)])
    >>> s
    0    POINT (1.00000 1.00000)
    1    POINT (2.00000 2.00000)
    2    POINT (3.00000 3.00000)
    dtype: geometry

    >>> s = geopandas.GeoSeries(
    ...     [Point(1, 1), Point(2, 2), Point(3, 3)], crs="EPSG:3857"
    ... )
    >>> s.crs  # doctest: +SKIP
    <Projected CRS: EPSG:3857>
    Name: WGS 84 / Pseudo-Mercator
    Axis Info [cartesian]:
    - X[east]: Easting (metre)
    - Y[north]: Northing (metre)
    Area of Use:
    - name: World - 85°S to 85°N
    - bounds: (-180.0, -85.06, 180.0, 85.06)
    Coordinate Operation:
    - name: Popular Visualisation Pseudo-Mercator
    - method: Popular Visualisation Pseudo Mercator
    Datum: World Geodetic System 1984
    - Ellipsoid: WGS 84
    - Prime Meridian: Greenwich

    >>> s = geopandas.GeoSeries(
    ...    [Point(1, 1), Point(2, 2), Point(3, 3)], index=["a", "b", "c"], crs=4326
    ... )
    >>> s
    a    POINT (1.00000 1.00000)
    b    POINT (2.00000 2.00000)
    c    POINT (3.00000 3.00000)
    dtype: geometry

    >>> s.crs
    <Geographic 2D CRS: EPSG:4326>
    Name: WGS 84
    Axis Info [ellipsoidal]:
    - Lat[north]: Geodetic latitude (degree)
    - Lon[east]: Geodetic longitude (degree)
    Area of Use:
    - name: World
    - bounds: (-180.0, -90.0, 180.0, 90.0)
    Datum: World Geodetic System 1984
    - Ellipsoid: WGS 84
    - Prime Meridian: Greenwich

    See Also
    --------
    GeoDataFrame
    pandas.Series

    """
    _metadata = ...
    def __new__(cls, data=..., index=..., crs=..., **kwargs): # -> Any | Series[Unknown]:
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def append(self, *args, **kwargs): # -> Any:
        ...
    
    @property
    def geometry(self): # -> GeoSeries:
        ...
    
    @property
    def x(self):
        """Return the x location of point geometries in a GeoSeries

        Returns
        -------
        pandas.Series

        Examples
        --------

        >>> from shapely.geometry import Point
        >>> s = geopandas.GeoSeries([Point(1, 1), Point(2, 2), Point(3, 3)])
        >>> s.x
        0    1.0
        1    2.0
        2    3.0
        dtype: float64

        See Also
        --------

        GeoSeries.y
        GeoSeries.z

        """
        ...
    
    @property
    def y(self):
        """Return the y location of point geometries in a GeoSeries

        Returns
        -------
        pandas.Series

        Examples
        --------

        >>> from shapely.geometry import Point
        >>> s = geopandas.GeoSeries([Point(1, 1), Point(2, 2), Point(3, 3)])
        >>> s.y
        0    1.0
        1    2.0
        2    3.0
        dtype: float64

        See Also
        --------

        GeoSeries.x
        GeoSeries.z

        """
        ...
    
    @property
    def z(self):
        """Return the z location of point geometries in a GeoSeries

        Returns
        -------
        pandas.Series

        Examples
        --------

        >>> from shapely.geometry import Point
        >>> s = geopandas.GeoSeries([Point(1, 1, 1), Point(2, 2, 2), Point(3, 3, 3)])
        >>> s.z
        0    1.0
        1    2.0
        2    3.0
        dtype: float64

        See Also
        --------

        GeoSeries.x
        GeoSeries.y

        """
        ...
    
    @classmethod
    def from_file(cls, filename, **kwargs): # -> GeoSeries:
        """Alternate constructor to create a ``GeoSeries`` from a file.

        Can load a ``GeoSeries`` from a file from any format recognized by
        `fiona`. See http://fiona.readthedocs.io/en/latest/manual.html for details.
        From a file with attributes loads only geometry column. Note that to do
        that, GeoPandas first loads the whole GeoDataFrame.

        Parameters
        ----------
        filename : str
            File path or file handle to read from. Depending on which kwargs
            are included, the content of filename may vary. See
            http://fiona.readthedocs.io/en/latest/README.html#usage for usage details.
        kwargs : key-word arguments
            These arguments are passed to fiona.open, and can be used to
            access multi-layer data, data stored within archives (zip files),
            etc.

        Examples
        --------

        >>> path = geopandas.datasets.get_path('nybb')
        >>> s = geopandas.GeoSeries.from_file(path)
        >>> s
        0    MULTIPOLYGON (((970217.022 145643.332, 970227....
        1    MULTIPOLYGON (((1029606.077 156073.814, 102957...
        2    MULTIPOLYGON (((1021176.479 151374.797, 102100...
        3    MULTIPOLYGON (((981219.056 188655.316, 980940....
        4    MULTIPOLYGON (((1012821.806 229228.265, 101278...
        Name: geometry, dtype: geometry

        See Also
        --------
        read_file : read file to GeoDataFame
        """
        ...
    
    @classmethod
    def from_wkb(cls, data, index=..., crs=..., **kwargs): # -> GeoSeries:
        """
        Alternate constructor to create a ``GeoSeries``
        from a list or array of WKB objects

        Parameters
        ----------
        data : array-like or Series
            Series, list or array of WKB objects
        index : array-like or Index
            The index for the GeoSeries.
        crs : value, optional
            Coordinate Reference System of the geometry objects. Can be anything
            accepted by
            :meth:`pyproj.CRS.from_user_input() <pyproj.crs.CRS.from_user_input>`,
            such as an authority string (eg "EPSG:4326") or a WKT string.
        kwargs
            Additional arguments passed to the Series constructor,
            e.g. ``name``.

        Returns
        -------
        GeoSeries

        See Also
        --------
        GeoSeries.from_wkt

        """
        ...
    
    @classmethod
    def from_wkt(cls, data, index=..., crs=..., **kwargs): # -> GeoSeries:
        """
        Alternate constructor to create a ``GeoSeries``
        from a list or array of WKT objects

        Parameters
        ----------
        data : array-like, Series
            Series, list, or array of WKT objects
        index : array-like or Index
            The index for the GeoSeries.
        crs : value, optional
            Coordinate Reference System of the geometry objects. Can be anything
            accepted by
            :meth:`pyproj.CRS.from_user_input() <pyproj.crs.CRS.from_user_input>`,
            such as an authority string (eg "EPSG:4326") or a WKT string.
        kwargs
            Additional arguments passed to the Series constructor,
            e.g. ``name``.

        Returns
        -------
        GeoSeries

        See Also
        --------
        GeoSeries.from_wkb

        Examples
        --------

        >>> wkts = [
        ... 'POINT (1 1)',
        ... 'POINT (2 2)',
        ... 'POINT (3 3)',
        ... ]
        >>> s = geopandas.GeoSeries.from_wkt(wkts)
        >>> s
        0    POINT (1.00000 1.00000)
        1    POINT (2.00000 2.00000)
        2    POINT (3.00000 3.00000)
        dtype: geometry
        """
        ...
    
    @property
    def __geo_interface__(self):
        """Returns a ``GeoSeries`` as a python feature collection.

        Implements the `geo_interface`. The returned python data structure
        represents the ``GeoSeries`` as a GeoJSON-like ``FeatureCollection``.
        Note that the features will have an empty ``properties`` dict as they
        don't have associated attributes (geometry only).

        Examples
        --------

        >>> from shapely.geometry import Point
        >>> s = geopandas.GeoSeries([Point(1, 1), Point(2, 2), Point(3, 3)])
        >>> s.__geo_interface__
        {'type': 'FeatureCollection', 'features': [{'id': '0', 'type': 'Feature', \
'properties': {}, 'geometry': {'type': 'Point', 'coordinates': (1.0, 1.0)}, \
'bbox': (1.0, 1.0, 1.0, 1.0)}, {'id': '1', 'type': 'Feature', \
'properties': {}, 'geometry': {'type': 'Point', 'coordinates': (2.0, 2.0)}, \
'bbox': (2.0, 2.0, 2.0, 2.0)}, {'id': '2', 'type': 'Feature', 'properties': \
{}, 'geometry': {'type': 'Point', 'coordinates': (3.0, 3.0)}, 'bbox': (3.0, \
3.0, 3.0, 3.0)}], 'bbox': (1.0, 1.0, 3.0, 3.0)}
        """
        ...
    
    def to_file(self, filename, driver=..., index=..., **kwargs): # -> None:
        """Write the ``GeoSeries`` to a file.

        By default, an ESRI shapefile is written, but any OGR data source
        supported by Fiona can be written.

        Parameters
        ----------
        filename : string
            File path or file handle to write to.
        driver : string, default: 'ESRI Shapefile'
            The OGR format driver used to write the vector file.
        index : bool, default None
            If True, write index into one or more columns (for MultiIndex).
            Default None writes the index into one or more columns only if
            the index is named, is a MultiIndex, or has a non-integer data
            type. If False, no index is written.

            .. versionadded:: 0.7
                Previously the index was not written.

        Notes
        -----
        The extra keyword arguments ``**kwargs`` are passed to fiona.open and
        can be used to write to multi-layer data, store data within archives
        (zip files), etc.

        See Also
        --------
        GeoDataFrame.to_file : write GeoDataFrame to file
        read_file : read file to GeoDataFame

        Examples
        --------

        >>> s.to_file('series.shp')  # doctest: +SKIP

        >>> s.to_file('series.gpkg', driver='GPKG', layer='name1')  # doctest: +SKIP

        >>> s.to_file('series.geojson', driver='GeoJSON')  # doctest: +SKIP
        """
        ...
    
    def __getitem__(self, key): # -> Any:
        ...
    
    @inherit_doc(pd.Series)
    def sort_index(self, *args, **kwargs): # -> Any:
        ...
    
    @inherit_doc(pd.Series)
    def take(self, *args, **kwargs): # -> Any:
        ...
    
    @inherit_doc(pd.Series)
    def select(self, *args, **kwargs): # -> Any:
        ...
    
    @inherit_doc(pd.Series)
    def apply(self, func, convert_dtype=..., args=..., **kwargs): # -> GeoSeries | Series[Unknown] | DataFrame:
        ...
    
    def __finalize__(self, other, method=..., **kwargs): # -> GeoSeries:
        """ propagate metadata from other to self """
        ...
    
    def isna(self): # -> Series[_bool]:
        """
        Detect missing values.

        Historically, NA values in a GeoSeries could be represented by
        empty geometric objects, in addition to standard representations
        such as None and np.nan. This behaviour is changed in version 0.6.0,
        and now only actual missing values return True. To detect empty
        geometries, use ``GeoSeries.is_empty`` instead.

        Returns
        -------
        A boolean pandas Series of the same size as the GeoSeries,
        True where a value is NA.

        Examples
        --------

        >>> from shapely.geometry import Polygon
        >>> s = geopandas.GeoSeries(
        ...     [Polygon([(0, 0), (1, 1), (0, 1)]), None, Polygon([])]
        ... )
        >>> s
        0    POLYGON ((0.00000 0.00000, 1.00000 1.00000, 0....
        1                                                 None
        2                             GEOMETRYCOLLECTION EMPTY
        dtype: geometry
        >>> s.isna()
        0    False
        1     True
        2    False
        dtype: bool

        See Also
        --------
        GeoSeries.notna : inverse of isna
        GeoSeries.is_empty : detect empty geometries
        """
        ...
    
    def isnull(self): # -> Series[_bool]:
        """Alias for `isna` method. See `isna` for more detail."""
        ...
    
    def notna(self): # -> Series[_bool]:
        """
        Detect non-missing values.

        Historically, NA values in a GeoSeries could be represented by
        empty geometric objects, in addition to standard representations
        such as None and np.nan. This behaviour is changed in version 0.6.0,
        and now only actual missing values return False. To detect empty
        geometries, use ``~GeoSeries.is_empty`` instead.

        Returns
        -------
        A boolean pandas Series of the same size as the GeoSeries,
        False where a value is NA.

        Examples
        --------

        >>> from shapely.geometry import Polygon
        >>> s = geopandas.GeoSeries(
        ...     [Polygon([(0, 0), (1, 1), (0, 1)]), None, Polygon([])]
        ... )
        >>> s
        0    POLYGON ((0.00000 0.00000, 1.00000 1.00000, 0....
        1                                                 None
        2                             GEOMETRYCOLLECTION EMPTY
        dtype: geometry
        >>> s.notna()
        0     True
        1    False
        2     True
        dtype: bool

        See Also
        --------
        GeoSeries.isna : inverse of notna
        GeoSeries.is_empty : detect empty geometries
        """
        ...
    
    def notnull(self): # -> Series[_bool]:
        """Alias for `notna` method. See `notna` for more detail."""
        ...
    
    def fillna(self, value=..., method=..., inplace=..., **kwargs):
        """Fill NA values with a geometry (empty polygon by default).

        "method" is currently not implemented for pandas <= 0.12.

        Examples
        --------

        >>> from shapely.geometry import Polygon
        >>> s = geopandas.GeoSeries(
        ...     [
        ...         Polygon([(0, 0), (1, 1), (0, 1)]),
        ...         None,
        ...         Polygon([(0, 0), (-1, 1), (0, -1)]),
        ...     ]
        ... )
        >>> s
        0    POLYGON ((0.00000 0.00000, 1.00000 1.00000, 0....
        1                                                 None
        2    POLYGON ((0.00000 0.00000, -1.00000 1.00000, 0...
        dtype: geometry

        >>> s.fillna()
        0    POLYGON ((0.00000 0.00000, 1.00000 1.00000, 0....
        1                             GEOMETRYCOLLECTION EMPTY
        2    POLYGON ((0.00000 0.00000, -1.00000 1.00000, 0...
        dtype: geometry

        >>> s.fillna(Polygon([(0, 1), (2, 1), (1, 2)]))
        0    POLYGON ((0.00000 0.00000, 1.00000 1.00000, 0....
        1    POLYGON ((0.00000 1.00000, 2.00000 1.00000, 1....
        2    POLYGON ((0.00000 0.00000, -1.00000 1.00000, 0...
        dtype: geometry

        See Also
        --------
        GeoSeries.isna : detect missing values
        """
        ...
    
    def __contains__(self, other): # -> bool_ | Literal[False]:
        """Allow tests of the form "geom in s"

        Tests whether a GeoSeries contains a geometry.

        Note: This is not the same as the geometric method "contains".
        """
        ...
    
    def plot(self, *args, **kwargs): # -> Axes:
        """Generate a plot of the geometries in the ``GeoSeries``.

        Wraps the ``plot_series()`` function, and documentation is copied from
        there.
        """
        ...
    
    def explode(self): # -> GeoSeries:
        """
        Explode multi-part geometries into multiple single geometries.

        Single rows can become multiple rows.
        This is analogous to PostGIS's ST_Dump(). The 'path' index is the
        second level of the returned MultiIndex

        Returns
        ------
        A GeoSeries with a MultiIndex. The levels of the MultiIndex are the
        original index and a zero-based integer index that counts the
        number of single geometries within a multi-part geometry.

        Examples
        --------
        >>> from shapely.geometry import MultiPoint
        >>> s = geopandas.GeoSeries(
        ...     [MultiPoint([(0, 0), (1, 1)]), MultiPoint([(2, 2), (3, 3), (4, 4)])]
        ... )
        >>> s
        0        MULTIPOINT (0.00000 0.00000, 1.00000 1.00000)
        1    MULTIPOINT (2.00000 2.00000, 3.00000 3.00000, ...
        dtype: geometry

        >>> s.explode()
        0  0    POINT (0.00000 0.00000)
           1    POINT (1.00000 1.00000)
        1  0    POINT (2.00000 2.00000)
           1    POINT (3.00000 3.00000)
           2    POINT (4.00000 4.00000)
        dtype: geometry

        See also
        --------
        GeoDataFrame.explode

        """
        ...
    
    def set_crs(self, crs=..., epsg=..., inplace=..., allow_override=...): # -> Series[Unknown] | GeoSeries:
        """
        Set the Coordinate Reference System (CRS) of a ``GeoSeries``.

        NOTE: The underlying geometries are not transformed to this CRS. To
        transform the geometries to a new CRS, use the ``to_crs`` method.

        Parameters
        ----------
        crs : pyproj.CRS, optional if `epsg` is specified
            The value can be anything accepted
            by :meth:`pyproj.CRS.from_user_input() <pyproj.crs.CRS.from_user_input>`,
            such as an authority string (eg "EPSG:4326") or a WKT string.
        epsg : int, optional if `crs` is specified
            EPSG code specifying the projection.
        inplace : bool, default False
            If True, the CRS of the GeoSeries will be changed in place
            (while still returning the result) instead of making a copy of
            the GeoSeries.
        allow_override : bool, default False
            If the the GeoSeries already has a CRS, allow to replace the
            existing CRS, even when both are not equal.

        Returns
        -------
        GeoSeries

        Examples
        --------
        >>> from shapely.geometry import Point
        >>> s = geopandas.GeoSeries([Point(1, 1), Point(2, 2), Point(3, 3)])
        >>> s
        0    POINT (1.00000 1.00000)
        1    POINT (2.00000 2.00000)
        2    POINT (3.00000 3.00000)
        dtype: geometry

        Setting CRS to a GeoSeries without one:

        >>> s.crs is None
        True

        >>> s = s.set_crs('epsg:3857')
        >>> s.crs  # doctest: +SKIP
        <Projected CRS: EPSG:3857>
        Name: WGS 84 / Pseudo-Mercator
        Axis Info [cartesian]:
        - X[east]: Easting (metre)
        - Y[north]: Northing (metre)
        Area of Use:
        - name: World - 85°S to 85°N
        - bounds: (-180.0, -85.06, 180.0, 85.06)
        Coordinate Operation:
        - name: Popular Visualisation Pseudo-Mercator
        - method: Popular Visualisation Pseudo Mercator
        Datum: World Geodetic System 1984
        - Ellipsoid: WGS 84
        - Prime Meridian: Greenwich

        Overriding existing CRS:

        >>> s = s.set_crs(4326, allow_override=True)

        Without ``allow_override=True``, ``set_crs`` returns an error if you try to
        override CRS.

        See Also
        --------
        GeoSeries.to_crs : re-project to another CRS

        """
        ...
    
    def to_crs(self, crs=..., epsg=...): # -> GeoSeries:
        """Returns a ``GeoSeries`` with all geometries transformed to a new
        coordinate reference system.

        Transform all geometries in a GeoSeries to a different coordinate
        reference system.  The ``crs`` attribute on the current GeoSeries must
        be set.  Either ``crs`` or ``epsg`` may be specified for output.

        This method will transform all points in all objects.  It has no notion
        or projecting entire geometries.  All segments joining points are
        assumed to be lines in the current projection, not geodesics.  Objects
        crossing the dateline (or other projection boundary) will have
        undesirable behavior.

        Parameters
        ----------
        crs : pyproj.CRS, optional if `epsg` is specified
            The value can be anything accepted
            by :meth:`pyproj.CRS.from_user_input() <pyproj.crs.CRS.from_user_input>`,
            such as an authority string (eg "EPSG:4326") or a WKT string.
        epsg : int, optional if `crs` is specified
            EPSG code specifying output projection.

        Returns
        -------
        GeoSeries

        Examples
        --------
        >>> from shapely.geometry import Point
        >>> s = geopandas.GeoSeries([Point(1, 1), Point(2, 2), Point(3, 3)], crs=4326)
        >>> s
        0    POINT (1.00000 1.00000)
        1    POINT (2.00000 2.00000)
        2    POINT (3.00000 3.00000)
        dtype: geometry
        >>> s.crs  # doctest: +SKIP
        <Geographic 2D CRS: EPSG:4326>
        Name: WGS 84
        Axis Info [ellipsoidal]:
        - Lat[north]: Geodetic latitude (degree)
        - Lon[east]: Geodetic longitude (degree)
        Area of Use:
        - name: World
        - bounds: (-180.0, -90.0, 180.0, 90.0)
        Datum: World Geodetic System 1984
        - Ellipsoid: WGS 84
        - Prime Meridian: Greenwich

        >>> s = s.to_crs(3857)
        >>> s
        0    POINT (111319.491 111325.143)
        1    POINT (222638.982 222684.209)
        2    POINT (333958.472 334111.171)
        dtype: geometry
        >>> s.crs  # doctest: +SKIP
        <Projected CRS: EPSG:3857>
        Name: WGS 84 / Pseudo-Mercator
        Axis Info [cartesian]:
        - X[east]: Easting (metre)
        - Y[north]: Northing (metre)
        Area of Use:
        - name: World - 85°S to 85°N
        - bounds: (-180.0, -85.06, 180.0, 85.06)
        Coordinate Operation:
        - name: Popular Visualisation Pseudo-Mercator
        - method: Popular Visualisation Pseudo Mercator
        Datum: World Geodetic System 1984
        - Ellipsoid: WGS 84
        - Prime Meridian: Greenwich

        See Also
        --------
        GeoSeries.set_crs : assign CRS

        """
        ...
    
    def estimate_utm_crs(self, datum_name=...):
        """Returns the estimated UTM CRS based on the bounds of the dataset.

        .. versionadded:: 0.9

        .. note:: Requires pyproj 3+

        Parameters
        ----------
        datum_name : str, optional
            The name of the datum to use in the query. Default is WGS 84.

        Returns
        -------
        pyproj.CRS

        Examples
        --------
        >>> world = geopandas.read_file(
        ...     geopandas.datasets.get_path("naturalearth_lowres")
        ... )
        >>> germany = world.loc[world.name == "Germany"]
        >>> germany.geometry.estimate_utm_crs()  # doctest: +SKIP
        <Projected CRS: EPSG:32632>
        Name: WGS 84 / UTM zone 32N
        Axis Info [cartesian]:
        - E[east]: Easting (metre)
        - N[north]: Northing (metre)
        Area of Use:
        - name: World - N hemisphere - 6°E to 12°E - by country
        - bounds: (6.0, 0.0, 12.0, 84.0)
        Coordinate Operation:
        - name: UTM zone 32N
        - method: Transverse Mercator
        Datum: World Geodetic System 1984
        - Ellipsoid: WGS 84
        - Prime Meridian: Greenwich
        """
        ...
    
    def to_json(self, **kwargs): # -> str:
        """
        Returns a GeoJSON string representation of the GeoSeries.

        Parameters
        ----------
        *kwargs* that will be passed to json.dumps().

        Returns
        -------
        JSON string

        Examples
        --------
        >>> from shapely.geometry import Point
        >>> s = geopandas.GeoSeries([Point(1, 1), Point(2, 2), Point(3, 3)])
        >>> s
        0    POINT (1.00000 1.00000)
        1    POINT (2.00000 2.00000)
        2    POINT (3.00000 3.00000)
        dtype: geometry

        >>> s.to_json()
        '{"type": "FeatureCollection", "features": [{"id": "0", "type": "Feature", "pr\
operties": {}, "geometry": {"type": "Point", "coordinates": [1.0, 1.0]}, "bbox": [1.0,\
 1.0, 1.0, 1.0]}, {"id": "1", "type": "Feature", "properties": {}, "geometry": {"type"\
: "Point", "coordinates": [2.0, 2.0]}, "bbox": [2.0, 2.0, 2.0, 2.0]}, {"id": "2", "typ\
e": "Feature", "properties": {}, "geometry": {"type": "Point", "coordinates": [3.0, 3.\
0]}, "bbox": [3.0, 3.0, 3.0, 3.0]}], "bbox": [1.0, 1.0, 3.0, 3.0]}'

        See Also
        --------
        GeoSeries.to_file : write GeoSeries to file
        """
        ...
    
    def to_wkb(self, hex=..., **kwargs): # -> Series[Unknown]:
        """
        Convert GeoSeries geometries to WKB

        Parameters
        ----------
        hex : bool
            If true, export the WKB as a hexadecimal string.
            The default is to return a binary bytes object.
        kwargs
            Additional keyword args will be passed to
            :func:`pygeos.to_wkb` if pygeos is installed.

        Returns
        -------
        Series
            WKB representations of the geometries

        See also
        --------
        GeoSeries.to_wkt
        """
        ...
    
    def to_wkt(self, **kwargs): # -> Series[Unknown]:
        """
        Convert GeoSeries geometries to WKT

        Parameters
        ----------
        kwargs
            Keyword args will be passed to :func:`pygeos.to_wkt`
            if pygeos is installed.

        Returns
        -------
        Series
            WKT representations of the geometries

        Examples
        --------
        >>> from shapely.geometry import Point
        >>> s = geopandas.GeoSeries([Point(1, 1), Point(2, 2), Point(3, 3)])
        >>> s
        0    POINT (1.00000 1.00000)
        1    POINT (2.00000 2.00000)
        2    POINT (3.00000 3.00000)
        dtype: geometry

        >>> s.to_wkt()
        0    POINT (1 1)
        1    POINT (2 2)
        2    POINT (3 3)
        dtype: object

        See also
        --------
        GeoSeries.to_wkb
        """
        ...
    
    def __xor__(self, other):
        """Implement ^ operator as for builtin set type"""
        ...
    
    def __or__(self, other):
        """Implement | operator as for builtin set type"""
        ...
    
    def __and__(self, other):
        """Implement & operator as for builtin set type"""
        ...
    
    def __sub__(self, other):
        """Implement - operator as for builtin set type"""
        ...
    


