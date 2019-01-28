#initialized repository
from shapely.geometry import Point, Polygon
import geopandas as gpd
import pandas as pd
vix = pd.read_file('vix-daily_json.json')
print(vix.head())


#simple tools to keep in mind
#p1 = Point(0,0) #point object created 
#print(p1)
#print(p1 == (0,0))
#polygon = Polygon([(0,0),(1,1),(1,0)])
