pipeline {

    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                    apt update
                    apt install -y python3 python3-pip

                    python3 --version

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
