pipeline {
    agent any
    stages {
        stage("entrada") {
            steps {
                sh "git clone https://github.com/hrchlhck/devsec.github.io.git"
            }
        }

        stage("meio") {
            steps {
                sh "python3 -m venv venv"
                sh ". venv/bin/activate"
                sh "pip install --upgrade pip"
                sh "pip install -r requirements.txt"
            }
        }

        stage("testes") {
            steps {
                sh "python -m unittest"
            }
        }

        stage("saida!") {
            steps {
                sh "deactivate"
            }
        }
    }
}