pipeline {
    agent any
    environment { 
        DATABASE_URI = credentials ('DATABASE_URI')
        SECRET_KEY = credentials('SECRET_KEY')
        DOCKER_LOGIN = credentials ('DOCKER_LOGIN')
    }
    stages {
        stage('Test') {
            steps { 
                sh 'bash jenkins/test.sh'
            }
        }
        stage('Setup Docker'){
            steps {
                sh 'bash jenkins/setup-docker.sh'
            }
        }
        stage('build') {
            steps {
                sh 'docker-compose build --parellel'
                sh 'docker login -u $DOCKER_LOGIN_USR -p-stdin $DOCKER_LOGIN_PSW'
                
            }
        }
        stage('push') {
            steps {
                sh 'docker-compose push'
            }
        }  
        stage('configuration') {
            steps {
                sh 'ansible-playbook -i inventory playbook.yaml'
                sh 'ansible-playbook -i config-swarm/inventory.yaml config-swarm/playbook.yaml'
            }
        }    
        stage('deploy') {
            steps {
                sh 'bash jenkins/deploy.sh'
           }
        }
        post{
            always{
                junit "junit/*.xml"
            cobertura coberturaReportFile: 'coverage.xml', fallNoReports:false 
            }
        }
    }