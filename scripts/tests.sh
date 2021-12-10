#!/bin/bash
#check the location
pwd

#install all dependencies
sudo update -y
sudo upgrade -y
sudo apt install -y python3-pip
sudo pip3 install --upgrade pip

#navigate to service1 folder, install dependencies and test it
cd flaskapp
pip3 install -r requirements.txt
python3 -m pytest --cov app
