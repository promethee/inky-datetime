#!/usr/bin/env python
# -*- coding: utf-8 -*-

from DateImg import DateImg
from waveshare_epd import epd2in13

epd = epd2in13.EPD()
epd.init(epd.lut_full_update)
epd.Clear(0xFF)

img = DateImg(
  epd.width,
  epd.height,
  "#000",
  (lambda: None),
  (lambda img: epd.display(epd.getbuffer(img)))
)
