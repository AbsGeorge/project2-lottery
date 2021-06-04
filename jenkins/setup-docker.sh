#!/bin/bash


# Install docker 
curl https://get.docker.com | sudo bash

#log into Docker 

 | docker login -u $DOCKER_LOGIN_USR -p-stdin $DOCKER_LOGIN_PSW