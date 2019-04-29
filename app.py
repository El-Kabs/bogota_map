import folium
import pandas
import json
from folium.map import *
from utiles import darTags, darPorTag

folium_map = folium.Map(location=[4.622, -74.06],
                        zoom_start=13,
                        tiles="Stamen Terrain")

with open('data.json', 'r', encoding="utf8") as f:
    jsonC = json.load(f)
    tags = []
    for x in jsonC['tags']:
        grupo = FeatureGroup(name=x['name'])
        restaurantes = darPorTag(x['id'])
        for x in restaurantes:
            grupo.add_child(Marker(x['location'][::-1], popup=(
                                   x['brand_name']+'\n <b>Precio: '+str(x['price_range'])+'</b>'
                                   +'\n <b>Horario: '+str(x['schedules'][0]['open_time'])+' - '+str(x['schedules'][0]['close_time'])+'</b>'),
                                   icon=folium.Icon(color='orange', icon='utensils', prefix='fa')))
        folium_map.add_child(grupo)
folium_map.add_child(folium.map.LayerControl())
folium_map.save("my_map.html")


