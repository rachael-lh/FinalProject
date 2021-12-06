#!/bin/bash
#check the location
pwd

#install all dependencies
sudo update -y
sudo upgrade -y
sudo apt install -y python3-pip
sudo pip3 install --upgrade pip