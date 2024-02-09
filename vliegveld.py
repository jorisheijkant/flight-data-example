# Libraries importeren
from traffic.data import opensky
import geopandas as gpd
from shapely.geometry import Point

# Al het verkeer van een vliegveld ophalen
schiphol_data = opensky.history(
    "2023-09-01 09:00",
    "2023-09-01 09:10",
    airport="EHAM",
    limit=10000 # Hiermee spelen om te kijken hoeveel data je nodig hebt
)

if schiphol_data is not None:
    # Dataframe maken, en opslaan als geojson
    # Het beste is om hierbij de punten om te zetten naar lijnen, zodat je de vliegroutes ziet
    df = schiphol_data.data
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude))
    gdf.to_file("schiphol.geojson", driver='GeoJSON')
else:
    print("Helaas konden we geen data vinden voor dit vliegveld en deze tijdsperiode.")
