#!/bin/bash
#check the location
pwd

#install all dependencies
sudo update -y
sudo upgrade -y
sudo apt install python3-pip
sudo pip3 install --upgrade pip
sudo usermod -aG docker $(whoami)

cd db
docker build -t db-finalproject .

cd ..

cd flask-app
pip3 install -r requirements.txt
docker build -t flask-app-finalproject . 

cd ..
docker-compose up -d