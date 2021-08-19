from io import BytesIO
from os.path import basename
from typing import Any, Dict, List

import morecantile

from flask import Blueprint, current_app, jsonify, Response, send_file
from morecantile.commons import Tile
from morecantile.models import TileMatrixSet
from rio_tiler.io.cogeo import COGReader
from rio_tiler.errors import TileOutsideBounds
from rio_tiler.models import ImageData
from rio_tiler.utils import render

imagery: Blueprint = Blueprint('imagery', __name__)

@imagery.route('/imagery-tiles')
def get_imagery_tiles() -> Response:
    image: COGReader = current_app.config.get('COG')
    tms: TileMatrixSet = morecantile.tms.get('WebMercatorQuad')
    data: Dict[str, Any] = {
        'file_name': basename(image.dataset.name),
        'min_zoom': image.minzoom,
        'max_zoom': image.maxzoom,
        'bbox': image.bounds,
        'tiles': []
    }
    zooms: List[int] = list(range(data.get('min_zoom'), data.get('max_zoom') + 1))
    tiles: List[Tile] = list(tms.tiles(*image.bounds, zooms=zooms))
    for tile in tiles:
        data['tiles'].append(
            {
                'x': tile.x,
                'y': tile.y,
                'z': tile.z
            }
        )
    return jsonify(data)

@imagery.route('/imagery/<int:z>/<int:x>/<int:y>.png')
def get_imagery(z: int, x: int, y: int) -> Response:
    image: COGReader = current_app.config.get('COG')
    out_of_bounds_tile = current_app.config.get('OOB')
    try:
        tile: ImageData = image.tile(x, y, z, tilesize=256)
        content = render(data=tile.data, mask=tile.mask, img_format='PNG')
        return send_file(
            #https://stackoverflow.com/questions/11017466/flask-to-return-image-stored-in-database
            BytesIO(content),
            mimetype='image/png'
        )
    except TileOutsideBounds:
        return send_file(
            BytesIO(out_of_bounds_tile),
            mimetype='image/png'
        )
