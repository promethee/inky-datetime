#!/bin/sh
apt-get update -y
apt-get upgrade -y
apt-get install fonts-dejavu python-pip python-pil python-numpy git ntpdate libopenjp2-7 libtiff5 libgl1-mesa-glx libatlas-base-dev -y
pip install --upgrade pip setuptools wheel
pip install inky pytz
sudo timedatectl set-ntp True
