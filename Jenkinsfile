pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                make doc
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