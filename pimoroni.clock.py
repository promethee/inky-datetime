#!/usr/bin/env python
# -*- coding: utf-8 -*-

from DateImg import DateImg
from inky import InkyPHAT

# Set up the display
inky_display = InkyPHAT("black")

# Uncomment the following if you want to rotate the display 180 degrees
inky_display.h_flip = True
inky_display.v_flip = True

img = DateImg(
  inky_display.WIDTH,
  inky_display.HEIGHT,
  inky_display.BLACK,
  (lambda img: inky_display.set_image(img)),
  (lambda img: inky_display.show(img))
)
