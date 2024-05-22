pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'python:3.8-slim'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.image("${DOCKER_IMAGE}").withRun('-v /var/run/docker.sock:/var/run/docker.sock') { c ->
                        sh "docker build -t my-python-app -f docker/Dockerfile ."
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.image("${DOCKER_IMAGE}").inside('--volume /var/run/docker.sock:/var/run/docker.sock') {
                        def pythonHome = tool name: 'Python 3.8', type: 'hudson.plugins.python.PythonInstallation'
                        sh "${pythonHome}/bin/python --version"
                        sh "${pythonHome}/bin/pip --version"
                        sh "${pythonHome}/bin/python -m unittest discover -s . -p '*Test.py'"
                    }
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

