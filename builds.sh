#!/bin/bash
#check the location
pwd

#install all dependencies
sudo apt update -y
sudo apt upgrade -y
sudo apt install -y python3-pip
sudo pip3 install --upgrade pip