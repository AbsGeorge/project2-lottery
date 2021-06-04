scp docker-compose.yaml docker:
ssh docker << EOF 
export SECRET_KEY=${SECRET_KEY}
export DATABASE_URI=${DATABASE_URI}
docker stak deploy --compose-file docker-compose.yaml app
dcoker exec loterry_numbers_server python3 create.py 