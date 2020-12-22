import folium
map = folium.Map(location=[6.598, 3.4141], zoom_start=6)

# Adding Points to the Map
fg = folium.FeatureGroup(name="My Map")

# Adding Multiple Points: To do this we use a for loop
for coordinates in [[6.578, 3.42], [6.432, 3.389]]:
    fg.add_child(folium.Marker(location=coordinates, popup="I am a Marker", icon=folium.Icon(color='blue')))


map.add_child(fg)
map.save("Map1.html")