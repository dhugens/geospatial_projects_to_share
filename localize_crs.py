import geopandas

def localize(input_gdf):
    local_crs = "EPSG:2877" # replace with applicable crs EPSG#
    if  input_gdf.crs == "None":
        input_gdf.crs = "EPSG:4326"
        input_gdf.to_crs(local_crs)
    else: 
        input_gdf.to_crs(local_crs)