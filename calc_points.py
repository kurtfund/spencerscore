import math

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

cities = {
    "London": (-0.12, 51.50),
    "Chennai": (80.27, 13.08),
    "Bangalore": (77.59, 12.97),
    "Dubai": (55.27, 25.20),
    "Czech": (16.60, 49.19),
    "Los Angeles": (-118.24, 34.05)
}

for name, (lon, lat) in cities.items():
    x, y = project(lon, lat)
    print(f"{name}: x={x:.1f}, y={y:.1f}")

