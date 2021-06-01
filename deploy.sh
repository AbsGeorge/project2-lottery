#!/bin/bash 

project_name=lottery_api

#Build Server 
docker build -t ${project_name}_server server 

#Build animal api
docker build -t ${project_name}_api lottery_number_api
docker build -t ${project_name}_api lottery_alpha_api

#create network 
docker network create ${project_name}_network 


#run containers
docker run -d \
  -p 5000:5000 \
  --name ${project_name}_server \
  --network ${project_name}_network \
  ${project_name}_server 


docker run -d \
  --name ${project_name}_api \
  --network ${project_name}_network \
  ${project_name}_api