pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..';
                make html
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}