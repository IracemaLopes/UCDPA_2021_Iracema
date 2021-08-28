import folium
#location is Canada
m=folium.Map(location=[59.787000283026565, -111.12920590302417], zoom_start=12)

#location is  Milan
m2=folium.Map(location=[45.457305121681685, 9.188590225926237], zoom_start=12)


#created marker in Vancouver
folium.Marker([49.289116777041166, -123.11142033962074],popup='Vancouver',
              tooltip='Canada Place',
              icon=folium.Icon(icon='heart', icon_color='red', color='green')).add_to(m)


#created marker in Duomo di Milano
folium.Marker([45.464195400558665, 9.191937227026742],popup='Cathedral',
              tooltip='Duomo di Milano',
              icon=folium.Icon(icon='camera', icon_color='red', color='green')).add_to(m2)

# we added a blue circle to indicate the area we like
folium.Circle(location =(49.272067602905764, -123.10193315953669),
    radius=800,
    popup='Love the area',
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(m)


#we added a blue circle to indicate the area we like in Milano city centre
folium.Circle(location =(45.46382094385277, 9.191974576083203),
    radius=800,
    popup='Love the area',
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(m2)

#generate a map in html
m.save('maps_Vancouver.html')
m2.save('map_Milan.html')