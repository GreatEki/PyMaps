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
fg = folium.FeatureGroup(name="My Map")

# Adding Multiple Points: To do this we use a for loop
for lt, ln, el in zip(lat, long, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+ " m", fill_color=color_producer(el), color='grey', fill_opacity=0.7, fill=True))

map.add_child(fg)
map.save("Map1.html")
# else:
# print('Path to file does not exist')




