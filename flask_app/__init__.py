import fiona
import geopandas

from flask import Flask
from geopandas.geodataframe import GeoDataFrame
from rio_tiler.io import COGReader

from flask_app.imagery.views import imagery
from flask_app.tracts.views import tracts

# https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/
def create_app() -> Flask:
    app: Flask = Flask(__name__)

    # TODO: Make sure 'image' gets closed after reading
    image: COGReader = COGReader(filepath="./data/homework_cog.tiff")

    out_of_bounds_tile = open("./data/out_of_bounds.png", "rb")
    oob = out_of_bounds_tile.read()
    out_of_bounds_tile.close()

    geopackage: GeoDataFrame = geopandas.read_file("./data/tracts.gpkg")

    app.config.from_mapping(COG=image, GPKG=geopackage, OOB=oob)

    app.register_blueprint(imagery)
    app.register_blueprint(tracts)

    return app
