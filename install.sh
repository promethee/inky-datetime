#!/bin/sh
apt-get update -y
apt-get upgrade -y
apt-get install python-pip python-pil python-numpy git ntpdate -y
pip install --upgrade pip setuptools wheel
pip install inky pytz
