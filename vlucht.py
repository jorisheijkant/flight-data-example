# Libraries importeren
from traffic.data import opensky
import geopandas as gpd
from shapely.geometry import Point

# Vlucht ophalen
vlucht = opensky.history(
    "2017-02-05 15:45",
    stop="2017-02-05 16:45",
    callsign="EZY158T",
    return_flight=True
)

if vlucht is not None:
    # Vlucht omzetten naar een GeoDataFrame en opslaan als geojson
    df = vlucht.data
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude))
    gdf.to_file("vlucht.geojson", driver='GeoJSON')
else:
    print("Helaas konden we geen data vinden voor deze vlucht en deze tijdsperiode.")