import geopandas as gpd

import nvdbapiv3 as nvdb
from nvdbapiv3 import nvdb2geojson


def get_data_from_vegkart(dataNumber, filterString):
    """Uses NVDB API to load data from SVVs Vegkart into a Geopandas DataFrame.    
    """
    data = nvdb.nvdbFagdata(dataNumber) # Trafikkregistreringsstasjoner
    data.filter({"egenskap": filterString})
    data_geo = nvdb2geojson.fagdata2geojson(data)
    df = gpd.GeoDataFrame.from_features(data_geo['features'])
    df.set_crs(epsg=25833)
    return df