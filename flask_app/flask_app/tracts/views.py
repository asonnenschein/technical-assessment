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

tracts: Blueprint = Blueprint('tracts', __name__)

MIN_Z: int = 0
MAX_Z: int = 15

@tracts.route('/tracts-tiles')
def get_tracts_tiles() -> Response:
    geopackage: GeoDataFrame = current_app.config.get('GPKG')
    bbox: ndarray[float, Any] = geopackage.geometry.total_bounds
    tms: TileMatrixSet = morecantile.tms.get('WebMercatorQuad')

    data: Dict[str, Any] = {
        'file_name': 'tracts.gpkg',
        'min_zoom': MIN_Z,
        'max_zoom': MAX_Z,
        'bbox': list(bbox),
        'tiles': []
    }

    zooms: List[int] = list(range(MIN_Z, MAX_Z + 1))
    tiles: List[Tile] = list(tms.tiles(*bbox, zooms=zooms))
    for tile in tiles:
        data['tiles'].append(
            {
                'x': tile.x,
                'y': tile.y,
                'z': tile.z
            }
        )
    return jsonify(data)

@tracts.route('/tracts/<int:z>/<int:x>/<int:y>.json')
def get_tracts(z: int, x: int, y: int) -> Response:
    geopackage: GeoDataFrame = current_app.config.get('GPKG')
    bbox: LngLatBbox = mercantile.bounds(mercantile.Tile(x=x, y=y, z=z))

    polygon = Polygon([
        (bbox.west,bbox.north),
        (bbox.west,bbox.south),
        (bbox.east,bbox.south),
        (bbox.west,bbox.north),
    ])

    clipped_gpkg: GeoDataFrame = geopandas.clip(geopackage, polygon)

    clipped_json = json.loads(clipped_gpkg.to_json())

    return jsonify(clipped_json)