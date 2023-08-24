pipeline {
    agent any
    stages {
        stage("Build") {
            steps {
                sh "python3 -m venv venv"
                sh "source venv/bin/activate"
                sh "pip3 install --upgrade pip"
                sh "pip3 install -r requirements.txt"
            }
        }

        stage("Tests") {
            steps {
                sh "venv/bin/python3 -m unittest"
            }
        }

        stage("Cleanup") {
            steps {
                sh "rm -rf ./venv"
            }
        }
    }
}
