pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'python:3.8-slim'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t my-python-app -f docker/Dockerfile ."
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Executando os testes unitários dentro do contêiner Docker
                    sh "docker run --rm -v ${WORKSPACE}:/app -w /app ${DOCKER_IMAGE} python3 -m unittest discover -s . -p '*Test.py'"
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


