pipeline {

    agent any

    stages {

        stage('Build') {

            steps {
                echo 'Building...'
                sh '''
                    sudo apt update
                    sudo apt install python3
                    sudo apt install python3-pip

                   '''
                sh 'python3 --version'
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
