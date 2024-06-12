pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clonar o repositório
                git 'https://github.com/cinquetti/S107atividade1.git'
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




