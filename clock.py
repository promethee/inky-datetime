#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from datetime import date
from datetime import datetime
import argparse

from PIL import Image, ImageDraw, ImageFont

from inky import InkyPHAT

PATH = os.path.dirname(__file__)

colour = "black"

# Set up the display
inky_display = InkyPHAT(colour)
inky_display.set_border(inky_display.BLACK)

fontSmall = ImageFont.truetype("DejaVuSansMono.ttf", 24)
fontBig = ImageFont.truetype("DejaVuSansMono.ttf", 32)

# Uncomment the following if you want to rotate the display 180 degrees
inky_display.h_flip = True
inky_display.v_flip = True

# Load our backdrop image
today = date.today()
now = datetime.now()
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
ImageDraw.Draw(img).text((0, 8), today.strftime(" %B %d"), inky_display.BLACK, font=fontBig)
ImageDraw.Draw(img).text((48, 56), now.strftime("%H:%M"), inky_display.BLACK, font=fontBig)

# Display the completed calendar on Inky pHAT
inky_display.set_image(img)
inky_display.show()
