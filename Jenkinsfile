pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'python:3.8-slim'
    }

    stages {
        stage('Build Docker Image') {
            agent {
                docker {
                    image 'docker:latest'
                    args '-v /var/run/docker.sock:/var/run/docker.sock'
                }
            }
            steps {
                echo 'Building Docker image...'
                script {
                    docker.build("${DOCKER_IMAGE}", '-f docker/Dockerfile .')
                }
            }
        }

        stage('Test') {
            agent {
                docker {
                    image "${DOCKER_IMAGE}"
                    reuseNode true
                }
            }
            steps {
                echo 'Testing...'
                script {
                    def pythonHome = tool name: 'Python 3.8', type: 'hudson.plugins.python.PythonInstallation'
                    sh "${pythonHome}/bin/python --version"
                    sh "${pythonHome}/bin/pip --version"
                    sh "${pythonHome}/bin/python -m unittest discover -s . -p '*Test.py'"
                }
            }
        }

        stage('Notification') {
            steps {
                echo 'Notification...'
                sh './jenkins.sh'
            }
        }
    }
}
