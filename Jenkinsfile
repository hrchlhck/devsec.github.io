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
                sh "pip3 install --upgrade pip"
                sh "pip3 install -r requirements.txt"
            }
        }

        stage("testes") {
            steps {
                sh "python3 -m unittest"
            }
        }

        stage("saida!") {
            steps {
                sh "ls "
            }
        }
    }
}