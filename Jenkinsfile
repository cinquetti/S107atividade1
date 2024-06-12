pipeline {
    agent any

    environment {
        DOCKER_VERSION = '20.10.8'
    }

    stages {
        stage('Checkout') {
            steps {
                // Clonar o repositório
                git branch: 'main', url: 'https://github.com/cinquetti/S107atividade1.git'
            }
        }

        stage('Install and Configure Docker') {
            steps {
                script {
                    // Verifica se o Docker já está instalado
                    def dockerVersion = sh(script: 'docker --version || true', returnStdout: true).trim()

                    if (!dockerVersion.startsWith('Docker version')) {
                        // Instalação do Docker
                        sh '''
                            curl -fsSL https://get.docker.com -o get-docker.sh
                            sh get-docker.sh
                            sudo usermod -aG docker jenkins
                            sudo systemctl start docker
                            sudo systemctl enable docker
                        '''
                        
                        // Verifica novamente a versão do Docker após a instalação
                        dockerVersion = sh(returnStdout: true, script: 'docker --version').trim()
                        echo "Docker installed successfully: ${dockerVersion}"
                    } else {
                        echo "Docker already installed: ${dockerVersion}"
                    }
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    // Construir a imagem Docker a partir do Dockerfile na pasta docker/
                    sh 'docker build -t my-python-app -f docker/Dockerfile .'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Rodar testes
                    sh 'docker run --rm my-python-app'
                }
            }
        }
    }
}




