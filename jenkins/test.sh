#install apt dependencies 
sudo apt-get update 
sudo apt-get install python3 python3-pip python3-venv -y

#create and source virtual environment 
python3 -m venv venv 
source venv/bin/activate 

#install pip requirements 
pip3 install -r requirements.txt

#run pytest
python3 -m pytest serviceone --cov=serviceone  --cov-repot=xml --junitxml=junit/test-results.xml
python3 -m pytest servicetwo --cov=servicetwo  --cov-repot=xml --junitxml=junit/test-results.xml
python3 -m pytest servicethree --cov=servicethree  --cov-repot=xml --junitxml=junit/test-results.xml
python3 -m pytest servicefour --cov=servicefour  --cov-repot=xml --junitxml=junit/test-results.xml
