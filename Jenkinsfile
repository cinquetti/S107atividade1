pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'python:3.8-slim'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker-compose -f docker-compose-jenkins.yml build'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Executando os testes unitários dentro do contêiner Docker
                    sh 'docker-compose -f docker-compose-jenkins.yml run --rm app python3 -m unittest discover -s . -p "*Test.py"'
                }
            }
        }

        stage('Notification') {
            steps {
                sh './jenkins.sh'
            }
        }
    }
}



