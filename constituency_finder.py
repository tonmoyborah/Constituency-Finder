from geopandas import GeoSeries, GeoDataFrame
from shapely.geometry import Polygon, Point, LineString


assembly_data = GeoDataFrame.from_file('/home/nikhil/ML/maps/assembly-constituencies/India_AC.shp')

# search in all data
test_point = Point(77.083493, 28.470082)
for index, row in assembly_data.iterrows():
    if row['geometry'].contains(test_point):
        print('constituency is {}'.format(row['AC_NAME']))
    else:
        continue


