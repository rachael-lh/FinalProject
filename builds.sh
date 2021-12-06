#!/bin/bash
#check the location
pwd

#install all dependencies
apt update -y
apt upgrade -y
apt install -y python3-pip
pip3 install --upgrade pip