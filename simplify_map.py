import json
import math
import re

with open('countries.json', 'r') as f:
    data = json.load(f)

width = 1600
height = 620

def project(lon, lat):
    lat = max(min(lat, 85), -85)
    lat_rad = lat * math.pi / 180
    y_merc = math.log(math.tan(math.pi/4 + lat_rad/2))
    y = height / 2 - (y_merc * height / 5.5)
    
    # Adjust X slightly to center better
    x = (lon + 180) * (width / 360)
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
        if len(poly[0]) < 10:
            continue
            
        for ring in poly:
            path_str = ""
            for i, (lon, lat) in enumerate(ring):
                x, y = project(lon, lat)
                cmd = "M" if i == 0 else "L"
                path_str += f"{cmd}{x:.1f},{y:.1f} "
            if path_str:
                path_str += "Z"
                paths.append(path_str)

svg_path = " ".join(paths)

with open('Spencer Scoring & Stage v4.html', 'r') as f:
    html = f.read()

# Replace the specific continents
# We know it starts with: <g filter="url(#map-glow)">
# and has <path d="M140,85
# We can find this exact block.
start_idx = html.find('<!-- Styled continents with smoother paths and glowing effect -->')
end_idx = html.find('</g>', start_idx) + 4

new_g = f"""<!-- Styled continents with smoother paths and glowing effect -->
      <g filter="url(#map-glow)" fill="rgba(184,144,74,.08)" stroke="rgba(184,144,74,.3)" stroke-width="1.5">
        <path d="{svg_path}" />
      </g>"""

if start_idx != -1 and end_idx != -1:
    html = html[:start_idx] + new_g + html[end_idx:]

with open('Spencer Scoring & Stage v4.html', 'w') as f:
    f.write(html)
print("HTML Map Updated!")
