cities = {
    "lon": ("LONDON", 799.5, 191.4),
    "la": ("LOS ANGELES", 274.5, 238.7),
    "cz": ("CZECH", 873.8, 198.5),
    "db": ("DUBAI", 1045.6, 258.7),
    "bg": ("BANGALORE", 1144.8, 284.3),
    "ch": ("CHENNAI", 1156.8, 284.0)
}

london = cities["lon"]

print('<g filter="url(#map-glow)">')
for code, (name, x, y) in cities.items():
    if code == "lon": continue
    # Calculate control points for a nice arching curve
    # mid point
    mx = (london[1] + x) / 2
    my = min(london[2], y) - abs(london[1] - x) * 0.15 - 20
    
    cp1x = london[1] + (x - london[1]) * 0.25
    cp1y = my
    cp2x = london[1] + (x - london[1]) * 0.75
    cp2y = my
    
    # Estimate length for stroke-dasharray
    dist = ((x - london[1])**2 + (y - london[2])**2)**0.5 * 1.2
    dist_int = int(dist + 50)
    
    print(f'  <path id="line-{code}" d="M{london[1]:.1f},{london[2]:.1f} C{cp1x:.1f},{cp1y:.1f} {cp2x:.1f},{cp2y:.1f} {x:.1f},{y:.1f}" stroke="#b8904a" stroke-width="2" fill="none" stroke-dasharray="{dist_int}" stroke-dashoffset="{dist_int}" opacity="0.8"/>')
print('</g>')

print(f'<circle id="c-lon" cx="{london[1]:.1f}" cy="{london[2]:.1f}" r="5" fill="#b8904a" filter="url(#map-glow)" opacity="0"/>')
print(f'<circle id="p-lon" cx="{london[1]:.1f}" cy="{london[2]:.1f}" r="5" fill="none" stroke="#b8904a" stroke-width="1" opacity="0"/>')
print(f'<text id="l-lon" x="{london[1]+10:.1f}" y="{london[2]-6:.1f}" font-family="\'Space Grotesk\',sans-serif" font-size="9" fill="#b8904a" letter-spacing="2" opacity="0">{london[0]}</text>')

for code, (name, x, y) in cities.items():
    if code == "lon": continue
    print(f'<circle id="c-{code}" cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#b8904a" opacity="0"/>')
    # Text placement: shift depending on location
    if code == "la":
        tx = x + 10; ty = y - 5
    elif code == "cz":
        tx = x + 10; ty = y - 5
    elif code == "db":
        tx = x + 10; ty = y - 5
    elif code == "bg":
        tx = x - 70; ty = y + 15
    elif code == "ch":
        tx = x + 10; ty = y + 5
    print(f'<text id="l-{code}" x="{tx:.1f}" y="{ty:.1f}" font-family="\'Space Grotesk\',sans-serif" font-size="9" fill="#b8904a" letter-spacing="2" opacity="0">{name}</text>')

