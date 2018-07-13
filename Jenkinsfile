pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Doc') {
            steps {
                echo 'Constructing doc ..'
                sh 'pip install sphinx_rtd_theme'
                sh 'make html'

                echo 'Doc ok'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}