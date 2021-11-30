pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh "aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 261110884830.dkr.ecr.us-east-2.amazonaws.com"
                sh "docker build -t 261110884830.dkr.ecr.us-east-2.amazonaws.com/test_project:backend backend"
                sh "docker build -t 261110884830.dkr.ecr.us-east-2.amazonaws.com/test_project:frontend frontend"
                sh "docker rmi $(docker images --filter 'dangling=true' -q --no-trunc)"

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