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
                sh "python -m unittest discover tests '*_test.py'"

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
                echo 'lalala'
            }
        }
    }
}