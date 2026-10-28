# this is a function to define chunk sizes using the call return from an api if item being called is a vector - to be used with the "go fetch.py" function
import requests
import geopandas as gpd

def def_chunks(target_url):
    response = requests.get(target_url)
    chunks_gdf = gpd.GeoDataFrame.from_features(response.json()["features"])
    chunk_size = len(chunks_gdf)
    return chunk_size