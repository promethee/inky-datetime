#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from datetime import date
from datetime import datetime
from pytz import timezone
import pytz
import argparse
from PIL import Image, ImageDraw, ImageFont
from inky import InkyPHAT

#PATH = os.path.dirname(__file__)
colour = "black"

# Set up the display
inky_display = InkyPHAT(colour)
inky_display.set_border(inky_display.BLACK)

# Uncomment the following if you want to rotate the display 180 degrees
inky_display.h_flip = True
inky_display.v_flip = True

w = inky_display.WIDTH
h = inky_display.HEIGHT

# Load our backdrop image
today = date.today()
now = datetime.now(tz=timezone("Europe/Paris"))
img = Image.new("P", (w, h))
draw = ImageDraw.Draw(img)

texts = [today.strftime("%B %d"), now.strftime("%H:%M")]
margin = 8
vertical_offsets = [margin / 4, h / 2 + margin / 4]
index = 0

for text in texts:
  fontsize = 100
  font = ImageFont.truetype("DejaVuSansMono.ttf", fontsize)
  size = draw.textsize(text, font)
  target_size = [w - margin, h / 2 - margin]
  while size[0] > w or size[1] > target_size[1]:
    #print("fontsize:", fontsize, "too large, reducing it and try again")
    fontsize = fontsize - 2
    font = ImageFont.truetype("DejaVuSansMono.ttf", fontsize)
    size = draw.textsize(text, font)
  horizontal_offset = (w / 2) - (size[0] / 2) - (margin / 2)
  draw.text((horizontal_offset, vertical_offsets[index]), text, inky_display.BLACK, font)
  index += 1

# Display the completed calendar on Inky pHAT
inky_display.set_image(img)
inky_display.show()
