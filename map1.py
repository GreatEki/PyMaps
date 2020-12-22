import folium
import pandas
import os

# if os.path.exists('volcano.txt'):
data = pandas.read_csv('volcano.txt')
lat = list(data['LAT'])
long = list(data['LON'])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation > 1000 and elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[6.598, 3.4141], zoom_start=6)
# Adding Points to the Map
# Feature Group for Volcanic Points
fgv = folium.FeatureGroup(name="Volcanic points")

# Adding Multiple Points: To do this we use a for loop
# we use the zip() method to pass multiple lists which we want to iterate on.
for lt, ln, el in zip(lat, long, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+ " m", fill_color=color_producer(el), color='grey', fill_opacity=0.7, fill=True))

# Adding GeoJson feature from a world.json file
# Feature Group for Population
fgp = folium.FeatureGroup(name='Population')
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function = lambda x: {"fillColor": "blue" if x['properties'] ['POP2005'] < 50000000 
else 'yellow' if x['properties'] ['POP2005'] > 50000000 and x['properties'] ['POP2005'] < 100000000 
else 'red'} ))

map.add_child(fgv)
map.add_child(fgp)
# Adding the folium layer control should be implemented after the Feature Group has been added to the map object
map.add_child(folium.LayerControl())
map.save("Map1.html")
# else:
# print('Path to file does not exist')




