import json
import math

with open('countries.json', 'r') as f:
    data = json.load(f)

width = 1600
height = 800

def project(lon, lat):
    # Equirectangular
    x = (lon + 180) * (width / 360)
    y = (180 - (lat + 90)) * (height / 180)
    # y is from 0 to 180 (lat -90 to 90). Actually, y = (90 - lat) * (height / 180)
    return x, y

paths = []
for feature in data.get('features', []):
    geom = feature.get('geometry')
    if not geom: continue
    gtype = geom.get('type')
    coords = geom.get('coordinates')
    
    polys = []
    if gtype == 'Polygon':
        polys = [coords]
    elif gtype == 'MultiPolygon':
        polys = coords
        
    for poly in polys:
        for ring in poly:
            path_str = ""
            for i, (lon, lat) in enumerate(ring):
                x = (lon + 180) * (width / 360)
                # Mercator approx for better look or just simple linear
                # Let's do simple linear with aspect ratio tweak
                y = (90 - lat) * (height / 180)
                # shift y slightly to match aesthetic
                
                cmd = "M" if i == 0 else "L"
                path_str += f"{cmd}{x:.1f},{y:.1f} "
            if path_str:
                path_str += "Z"
                paths.append(path_str)

with open('map_path.txt', 'w') as f:
    f.write(" ".join(paths))

