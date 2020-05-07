#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from datetime import date
from datetime import datetime
from pytz import timezone
import pytz
from PIL import Image, ImageDraw, ImageFont

def DateImg(w, h, color, set_img, show_img):
  # Load our backdrop image
  today = date.today()
  now = datetime.now(tz=timezone("Europe/Paris"))
  img = Image.new("P", (w, h))
  draw = ImageDraw.Draw(img)
  texts = [today.strftime("%B %d"), now.strftime("%H:%M")]
  margin = 4
  vertical_offsets = [margin / 4, h / 2 + margin / 4]
  index = 0

  for text in texts:
    fontsize = 100
    font = ImageFont.truetype("DejaVuSansMono.ttf", fontsize)
    size = draw.textsize(text, font)
    target_size = [w - margin, h / 2 - margin]
    while size[0] > w or size[1] > target_size[1]:
      fontsize = fontsize - 2
      font = ImageFont.truetype("DejaVuSansMono.ttf", fontsize)
      size = draw.textsize(text, font)
    print("using fontsize:", fontsize)
    horizontal_offset = (w / 2) - (size[0] / 2) - (margin / 2)
    draw.text((horizontal_offset, vertical_offsets[index]), text, color, font)
    index += 1
  set_img(img)
  show_img(img)
