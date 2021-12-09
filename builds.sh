#!/bin/bash
#check the location
pwd

#install all dependencies
sudo update -y
sudo upgrade -y
sudo apt install python3-pip
sudo pip3 install --upgrade pip

cd flask-app
pip3 install -r requirements.txt
sudo usermod -aG docker $(whoami)
cd ..
docker-compose up -d