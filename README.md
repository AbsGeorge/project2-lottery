# Practical Project: Lottery

## Contents
* [Introduction](#introduction) 
  * [Objective](#objective)
  * [Proposal](#proposal)
* [Architecture](#architecture)
  * [Risk Assessment](#risk-assessment)
  * [Trello Board](#Trello-board)
  * [Unit Testing](#Unit-Test-Analysis)
* [Infrastructure](#infrastructure)
  * [Jenkins](#jenkins)
  * [Entity Diagram](#entity-diagram)
* [Development](#development)
  * [Front-End Design](#front-end)


## Introduction

### Objective
The objective provided for this project is as follows:
> To create a service-orientated architecture for your application, this application must be composed of at least 4 services that work together.

Service 1
The core service – this will render the Jinja2 templates you need to interact with your application, it will also be responsible for communicating with the other 3 services, and finally for persisting some data in an SQL database.

Service #2 + #3
These will both generate a random “Object” each. 

Service #4
This service will also create an “Object” however this “Object” must be based upon the results of service #2 and #3 using some pre-defined rules.

The following constraints were also set:
* Kanban Board: Asana or an equivalent Kanban Board
* Version Control: Git - using the feature-branch model
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Reverse Proxy: NGINX
* Database Layer: MySQL

### Proposal
To meet all of the requirements and to ensure the MVP was produced in the time-frame provided, I first had to realise that the importance of this project was the infrastructure and implementation of my CI/CD. This means the application itself is less important, and so the proposal is fairly trivial.

#### Lottery 
* Service 1 (front-end): Allows user to input 5 numbers and 2 alphabets.
* Service 2: generates and returns 5 random numbers 
* Service 3: generates and returns 2 random alphabets 
* Service 4: combines the results from service 2 and service 3 and compares it with the user input from service 1 to determine if player wins or losses. 

## Architecture
### Risk Assessment
I created a risk assessment to analyse any factors that may cause a risk to the project. 
Below is an image of my detailed risk assessment, which outlines the minor and major risks that have potential to impact the success of this project. 

![Risk Assessment](https://i.gyazo.com/4b8584f239045301ad800545c6022b14.png)

*Highlighted rows are risks that were discovered as the project progressed.*  
View the original document [here](https://docs.google.com/spreadsheets/d/1olqQSJ7y09J8EA4TxXEmbGOleK4tgDaq/edit#gid=648475153)

### Trello Board
My project tracking board can be seen below. 

![trello board image](https://i.gyazo.com/f86b39dca04c4dc275e87fd81a3fa62d.jpg)

View the original board [here](https://trello.com/b/mkSUq0gB/lottery)

### Unit Test Analysis 
Testing is an essential part of any successful project and given the time frame, the most feasible and straight-forward method I used was unit-testing. 

I used pytest to run the unit tests on the 4 services. These are designed to determine if a certain function is running as expected. Jenkins produces console outputs that will inform me if any of what I intended each of the 4 services to either passed or failed. 

A total of 4 unit tests were run for each service and Looking at the pipeline image below, they all passed. This is because the pipeline process will breakdown if any of the stages failed.

 
![Pipeline] (https://i.gyazo.com/4b4789661293d4c55c8d9f3a6444169b.png)

I have selected images of random services (1 and 2) below, the display the successfull unit testing and the percentage coverage of testing. 

![Service3 Unit Testing](https://i.gyazo.com/4e2b4b6aeae1dc5908f1f3632fcb14c6.png)

![test coverage of frontend server](https://i.gyazo.com/58c0556294165cbf0e5ea34c4ce2bb49.png)

The exact syntax used for the testing is as below:

 > * python3 -m pytest serviceone --cov=serviceone  --cov-report=xml --junitxml=junit/test-results.xml
 > * python3 -m pytest servicetwo --cov=servicetwo  --cov-report=xml --junitxml=junit/test-results.xml
 > * python3 -m pytest servicethree --cov=servicethree  --cov-report=xml --junitxml=junit/test-results.xml
 > * python3 -m pytest servicefour --cov=servicefour  --cov-report=xml --junitxml=junit/test-results.xml



## Infrastructure
Below is the Continuous integration used in my project. The focus is speed and efficiency from application, _including any future changes in code_, development-to-deployment. As code is pushed to my GitHub repository, Jenkins fetches and builds the code in my repository. Jenkins will then run any pre written unit and integration testing in a testing environment and with pre-installed plugins, Jenkins is then able to produce reports on how the application is performing.  

### Jenkins
Whenever new content is pushed to the `version1` branch, Github will send a webhook to Jenkins which tells it to run the following pipeline:

#### Test: pytest  
>  A coverage report is produced and can be viewed in the console logs. 

#### Build & Push: docker-compose  
> Jenkins' credentials system is used to handle logging into DockerHub, and the new images are then pushed to the repository specified.

#### Configure: ansible 
> * Installed ansible and run the ansible playbook which contained:  
###### Setting up the swarm, and joining the swarm on all worker nodes,
###### Setting up Nginx as a load balancer.

#### Deploy: docker swarm/stack 
> * Jenkins exports all environment variables ( database and secret key)
> * Jenkins copies the `docker-compose.yaml` file over to the manager node, SSH's onto it, and then runs `docker stack deploy`.

 
![cicd pipeline image](https://i.gyazo.com/fa9a04ce4c357369103cc7bea3a77c56.png)


#### **6.** Load Balancer: Nginx 
> * The N+ icon is nginx. It is being used as a load balancer and is confiqured with ansible to distribute the workload amongst the nodes within the docker swarm. For the purpose of this task, I did not reduce the workload of any node within the swarm. 

#### **7.** Website building and Templating: Flask and Jinja2 
> * Flask was used to build the website and jinja2 is used to build the website templates.  

### Entity Diagram
Below is a very simple entity relational diagram that I used for my project. 

![entitity diagram image](https://i.gyazo.com/0904920c98bc0fab95f3f0bb762cea10.png)

The information will be gather and stored via the following processes: 

 > * Service 1 will intake information from the user (player_numbers) as well as information from service two and service 3
 > * Service 2 will generate random lottery numbers (lotnum) and pass it to service 1
 > * Service 3 will generate random alphabets (lotalpa) and pass it to service 1
 > * Service 4 will take a post request from service one, interact with the database and store these information, followed by comparing the results. 

 ![Service Interaction](https://i.gyazo.com/e75b99bede09810cba0d970c379520eb.png)
 


## Development
### Front-End

Home Page 

![image of front-end](https://i.gyazo.com/f45d5b7ad6a84bd34af3c32195224987.png)

Results Page 

![Display After a User Inputs Data](https://i.gyazo.com/d169a0e082a2e26c8f86f03774256ac4.png)




## Footer
### Future Improvements
* A maximum amount a player can play the game. 
* A more user friendly Interface
* A smoother continous integration with efficient version updates 


### Author
Abs Pinnankoh-Morrison 

### Acknowledgements
* Oliver Nichols
* Harry Volker

