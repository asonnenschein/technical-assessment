## Data Preparation

### Requirements
The workflows described herein this document require installation of popular geospatial Unix command line software tools:

GDAL and OGR OSX installation:
```
brew install gdal
```

rio-cogeo OSX (Python) installation:
```
pip install rio-cogeo
```

### External Documentation
More in-depth technical documentation about the workflows described herein this document can be found at:
- https://gdal.org/drivers/vector/gpkg.html
- https://gdal.org/drivers/raster/cog.html
- https://cogeotiff.github.io/rio-cogeo/Is_it_a_COG/

### Convert homework.geojson to tracts.gpkg
1. Validate that OGR recognizes input `homework.geojson` file as compatible with GeoJSON driver:
```
ogrinfo homework.geojson
```

2. Convert `homework.geojson` to GPKG file named `tracts`:
```
ogr2ogr -f GPKG tracts.gpkg homework.geojson
```

3. Validate that OGR recgnizes output `tracts.gpkg` file as compatible with GPKG driver:
```
ogrinfo tracts.gpkg
```

### Convert homework.tiff to homework_cog.tiff
1. Validate that GDAL recognizes input `homework.tiff` file as compatible with GeoTIFF (GTiff) driver:
```
gdalinfo homework.tiff
```

2. Strip NIR band off input `homework.tiff` by creating a copy of the file called `homework_rgb.tiff` that only includes RGB bands.  The ultimate goal with this data is to serve it as PNG tiles, and the GDAL PNG driver does not support NIR bands.  If the NIR band is not removed, a 'red herring' error will be thrown when attempting to render the PNG (it's a red herring error because it will say that the PNG driver doesn't support 5 band imagery - but there are only 4 bands on the image and the issue is really the incompatible NIR band):
```
gdal_translate -b 1 -b 2 -b 3 homework.tiff homework_rgb.tiff
```

3. Convert `homework_rgb.tiff` to COG file named `homework_cog.tiff`:
GDAL Example
```
gdal_translate homework_rgb.tiff homework_cog.tiff -of COG 
```

rio-cogeo Example:
```
rio cogeo create homework_rgb.tiff homework_cog_rio.tiff
```

4. Validate output `homework_cog.tiff` COG:
```
rio cogeo validate homework_cog.tiff
```