#!/bin/bash
#check the location
pwd

#install all dependencies
pip3 install --upgrade docker
docker build -t flask-app-finalproject .