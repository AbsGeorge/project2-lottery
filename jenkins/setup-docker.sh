#!/bin/bash


# Install docker 
curl https://get.docker.com | sudo bash
sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Add jenkins to docker group 
sudo usermod -aG docker jenkins 

#log into Docker 

docker login -u $DOCKER_LOGIN_USR -p-stdin $DOCKER_LOGIN_PSW