scp docker-compose.yaml swarm-master:
ssh swarm-master << EOF 
export SECRET_KEY=${SECRET_KEY}
export DATABASE_URI=${SQLALCHEMY_DATABASE_URI}
docker stack deploy --compose-file docker-compose.yaml 
docker exec lottery_numbers_server python3 create.py 