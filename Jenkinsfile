pipeline {
    agent {
        docker {
            image 'python:3.8-slim'
        }
    }

    stages {
        stage('Setup') {
            steps {
                echo 'Setting up environment...'
                sh 'python3 --version'
                sh 'pip3 --version'
                sh '''
                    cd ${WORKSPACE}
                    ls
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Testing...'
                sh '''
                    cd ${WORKSPACE}
                    # Instalar dependências do projeto, se houver um requirements.txt
                    if [ -f requirements.txt ]; then
                        pip3 install -r requirements.txt
                    fi
                    # Executar testes unitários
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