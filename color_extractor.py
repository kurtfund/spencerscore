from PIL import Image
from collections import Counter
import sys

def get_colors(img_path):
    img = Image.open(img_path).convert('RGB')
    img.thumbnail((200, 200))
    colors = list(img.getdata())
    counts = Counter(colors)
    print(img_path)
    
    greenest_color = None
    max_green_ratio = 0
    
    for c, count in counts.items():
        r, g, b = c
        if g > r + 10 and g > b + 10 and g > 50:
            ratio = g / max(1, r + b)
            if ratio > max_green_ratio:
                max_green_ratio = ratio
                greenest_color = c
    
    if greenest_color:
        print(f"Greenest: {greenest_color}, hex #{greenest_color[0]:02x}{greenest_color[1]:02x}{greenest_color[2]:02x}")
    else:
        print("No green found")

get_colors("uploads/hf_20260422_192914_4c75f682-99af-498b-a1b0-a9028b4b6084.png")
