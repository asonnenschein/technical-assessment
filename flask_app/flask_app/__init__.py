from flask import Flask
from rio_tiler.io import COGReader

from flask_app.imagery.views import imagery

#https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/
def create_app() -> Flask:
    app: Flask = Flask(__name__)
    # TODO: Make sure 'image' gets closed after reading
    image: COGReader = COGReader(filepath='../data/homework_cog.tiff')
    out_of_bounds_tile = open('../data/out_of_bounds.png', 'rb')
    oob = out_of_bounds_tile.read()
    out_of_bounds_tile.close()
    app.config.from_mapping(
        COG=image,
        OOB=oob
    )
    app.register_blueprint(imagery)
    return app
