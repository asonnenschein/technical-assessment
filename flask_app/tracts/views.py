import json

from typing import Any, Dict, List

import geopandas
import mercantile
import morecantile
from numpy import ndarray

from geopandas.geodataframe import GeoDataFrame
from mercantile import LngLatBbox
from morecantile.commons import Tile
from morecantile.models import TileMatrixSet
from shapely.geometry import Polygon

from flask import Blueprint, current_app, jsonify, Response

tracts: Blueprint = Blueprint("tracts", __name__)

MIN_Z: int = 0
MAX_Z: int = 15

# Flask will resolve to GET HTTP method by default when the 'methods' parameter is not included in the 'Blueprint.route()' method
@tracts.route("/tracts-tiles")
def get_tracts_tiles() -> Response:
    """Produces metadata about available JSON XYZ tiles within the extent of the GPKG dataset that is cached in-memory
    on the server at startup time.

    Returns:
        Response: Flask HTTP response object with content-type 'application/json'
    """

    geopackage: GeoDataFrame = current_app.config.get("GPKG")
    bbox: ndarray[float, Any] = geopackage.geometry.total_bounds
    tms: TileMatrixSet = morecantile.tms.get("WebMercatorQuad")

    data: Dict[str, Any] = {
        "file_name": "tracts.gpkg",
        "min_zoom": MIN_Z,
        "max_zoom": MAX_Z,
        "bbox": list(bbox),
        "tiles": [],
    }

    zooms: List[int] = list(range(MIN_Z, MAX_Z + 1))
    tiles: List[Tile] = list(tms.tiles(*bbox, zooms=zooms))
    for tile in tiles:
        data["tiles"].append({"x": tile.x, "y": tile.y, "z": tile.z})
    return jsonify(data)


# Flask will resolve to GET HTTP method by default when the 'methods' parameter is not included in the 'Blueprint.route()' method
@tracts.route("/tracts/<int:z>/<int:x>/<int:y>.json")
def get_tracts(z: int, x: int, y: int) -> Response:
    """Fetches individual JSON XYZ map tiles based on controller input.  Tiles are sourced from the GPKG dataset that
    is cached in-memory on the server at startup time, and are rendered on-the-fly as JSON.  If input XYZ location does
    not fall within the bounds of the GPKG, an empty JSON object is returned by default.

    Args:
        z (int): Zoom level of tile
        x (int): Location of tile on horizontal x-axis
        y (int): Location of tile on vertical y-axis

    Returns:
        Response: Flask HTTP response with content-type 'application/json'
    """
    try:
        geopackage: GeoDataFrame = current_app.config.get("GPKG")
        bbox: LngLatBbox = mercantile.bounds(mercantile.Tile(x=x, y=y, z=z))
        polygon = Polygon(
            [
                (bbox.west, bbox.north),
                (bbox.west, bbox.south),
                (bbox.east, bbox.south),
                (bbox.west, bbox.north),
            ]
        )
        clipped_gpkg: GeoDataFrame = geopandas.clip(geopackage, polygon)
        clipped_json = json.loads(clipped_gpkg.to_json())
        return jsonify(clipped_json)
    except OverflowError:
        return jsonify({})
