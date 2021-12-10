#!/bin/bash
#check the location
pwd

#install all dependencies
sudo update -y
sudo upgrade -y
sudo apt install python3-pip
sudo pip3 install --upgrade pip
sudo usermod -aG docker $(whoami)

docker-compose down --rmi all	
docker-compose up -d