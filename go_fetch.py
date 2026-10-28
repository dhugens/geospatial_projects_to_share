# functino to call all records within a dataset when limited by an api chunk size
import requests
import geopandas as gpd 

def fetch_all_records(base_url, chunk_size): #chunk size < len(records)
    features = []
    offset = 0
    
    while True:
        query_url = f"{base_url}&resultOffset={offset}&resultRecordCount={chunk_size}"
        response = requests.get(query_url)
        response.raise_for_status()  # anyone home?
        
        data = response.json()
        features.extend(data['features'])
        
        # stop if fewer features were returned than the chunk size
        if len(data['features']) < chunk_size:
            break
        
        # offset for the next batch
        offset += chunk_size
        
    # convert to gdf
    return gpd.GeoDataFrame.from_features(features)