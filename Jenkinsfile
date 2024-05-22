pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'python-app'
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
                    docker.build(DOCKER_IMAGE, '-f Dockerfile .')
                }
            }
        }

        stage('Test') {
            agent {
                docker {
                    // Use a imagem Docker criada acima
                    image "${DOCKER_IMAGE}:latest"
                }
            }
            steps {
                echo 'Testing...'
                sh '''
                    python3 --version
                    pip --version
                    cd ${WORKSPACE}
                    python3 -m unittest discover -s . -p "*Test.py"
                '''
            }
        }

        stage('Notification') {
            steps {
                echo 'Notification...'
                sh '''
                    cd scripts
                    chmod 775 *
                    ./jenkins.sh
                '''
            }
        }
    }
}
