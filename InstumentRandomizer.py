import os
import random
from PIL import Image, ImageDraw, ImageFont

LIB_PATH = "/Library/Application Support/Logic/Plug-In Settings"
all_files = []
for root, dirs, files in os.walk(LIB_PATH):
    for file in files:
        if(file.endswith(".acp")):
            all_files.append(file[:-4])
            
Scales = ["G Flat", "D Flat", "A Flat", "E Flat", "B Flat", "F", "C", "G", "D", "A", "E", "B"]


width, height = 800, 300
image = Image.new('RGB', (width, height), color=(248, 250, 255))
draw = ImageDraw.Draw(image)

font = ImageFont.truetype("PlantagenetCherokee.ttf", 40)

texts = [f"Instrument: {random.choice(all_files)}", f"Mod: {random.choice(range(1,9))}",f"Key: {random.choice(Scales)}"]
text_positions = [(40, 50), (40, 100), (40, 150)]

def random_color():
    return (random.choice(range(256)), random.choice(range(256)), random.choice(range(256)))

for i in range(3):
    draw.text(text_positions[i], texts[i], fill=random_color(), font=font)

image.show()