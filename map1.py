import folium
import pandas
import os

if os.path.exists('volcano.txt'):
    data = pandas.read_csv('volcano.txt')
    lat = list(data['LAT'])
    long = list(data['LON'])
    map = folium.Map(location=[6.598, 3.4141], zoom_start=6)
    # Adding Points to the Map
    fg = folium.FeatureGroup(name="My Map")

    # Adding Multiple Points: To do this we use a for loop
    for lt, ln in zip(lat, long):
        fg.add_child(folium.Marker(location=[lt, ln], popup="I am a Marker", icon=folium.Icon(color='blue')))
    
    map.add_child(fg)
    map.save("Map1.html")
else:
    print('Path to file does not exist')




