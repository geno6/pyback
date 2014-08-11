#!/bin/sh

# Apt install necessary packages

sudo apt-get -y update

sudo apt-get -y install python-dev libevent-dev python3-pil python3-setuptools

# Install pip3.4

sudo easy_install3 pip

# Install requirements

sudo pip3.4 install -r requirements.txt

exit