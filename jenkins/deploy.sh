scp docker-compose.yaml swarm-master:
ssh swarm-master << EOF 
export SECRET_KEY=${SECRET_KEY}
export DATABASE_URI=${DATABASE_URI}
docker stack deploy --compose-file docker-compose.yaml lottery_numbers_stack
EOF