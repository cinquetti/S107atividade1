pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clonar o repositório
                git branch: 'main', url: 'https://github.com/cinquetti/S107atividade1.git'
            }
        }

        stage('Install Docker') {
            steps {
                script {
                    // Verifica se o Docker já está instalado
                    def dockerVersion = sh(returnStdout: true, script: 'docker --version || true').trim()

                    if (dockerVersion.startsWith('Docker version')) {
                        echo "Docker already installed: ${dockerVersion}"
                    } else {
                        // Instalação do Docker no Ubuntu/Debian
                        sh '''
                            sudo apt-get update
                            sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
                            curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
                            sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
                            sudo apt-get update
                            sudo apt-get install -y docker-ce docker-ce-cli containerd.io
                            sudo systemctl start docker
                            sudo systemctl enable docker
                        '''
                        
                        // Verifica novamente a versão do Docker após a instalação
                        dockerVersion = sh(returnStdout: true, script: 'docker --version').trim()
                        echo "Docker installed successfully: ${dockerVersion}"
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




