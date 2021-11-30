pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'docker images -q -f dangling=true | xargs --no-run-if-empty docker rmi'
                sh "aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 261110884830.dkr.ecr.us-east-2.amazonaws.com"
                sh "docker build -t 261110884830.dkr.ecr.us-east-2.amazonaws.com/test_project:backend backend"
                sh "docker build -t 261110884830.dkr.ecr.us-east-2.amazonaws.com/test_project:frontend frontend"

            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh "docker network create --driver=bridge --subnet=192.168.0.0/16 testnet"
                sh "AWS_ACCESS_KEY_ID=\$(curl http://169.254.169.254/latest/meta-data/iam/security-credentials/fenkins-for-ecs-role | jq .AccessKeyId)"
                sh "echo AWS_ACCESS_KEY_ID=\${AWS_ACCESS_KEY_ID} >> env"
                sh "AWS_SECRET_ACCESS_KEY=\$(curl http://169.254.169.254/latest/meta-data/iam/security-credentials/fenkins-for-ecs-role | jq .SecretAccessKey)"
                sh "echo AWS_SECRET_ACCESS_KEY=\${AWS_SECRET_ACCESS_KEY} >> env"
                sh "AWS_SESSION_TOKEN=\$(curl http://169.254.169.254/latest/meta-data/iam/security-credentials/fenkins-for-ecs-role | jq .Token)"
                sh "echo AWS_SESSION_TOKEN=\${AWS_SESSION_TOKEN} >> env"
                sh "echo  S3_BUCKET=testprojectmessages >> env"
                sh "echo MESSAGES_FILE=messages.txt >> env"
                sh "echo  AWS_REGION_NAME=us-east-2 >> env"
                sh "echo  FRONTEND_URL=192.168.0.3 >> env"
                sh "docker run -d --network=testnet --ip=192.168.0.2  --env-file env 261110884830.dkr.ecr.us-east-2.amazonaws.com/test_project:backend"
                sh "docker run -d --network=testnet --ip=192.168.0.3  --env BACKEND_URL=http://192.168.0.2 261110884830.dkr.ecr.us-east-2.amazonaws.com/test_project:frontend"
                sh "if curl 192.168.0.3 | grep 'input type=\"text\" name=\"message\"'; then echo \"frontend is working\"; else exit 1; fi"
                sh "if  curl -X POST -F \"message=mymessage\" http://192.168.0.3/message/save | grep 'Your message saved'; then echo \"backend is working\"; else exit 1; fi"
                sh "rm env"
                sh "docker stop \$(docker ps -qa)"
                sh "docker rm \$(docker ps -qa)"
                sh "docker network rm testnet"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh "docker push 261110884830.dkr.ecr.us-east-2.amazonaws.com/test_project:backend"
                sh "docker push 261110884830.dkr.ecr.us-east-2.amazonaws.com/test_project:frontend"
                sh "docker logout"
                sh "docker system prune -fa"
                sh "aws ecs update-service --service backend"
                sh "aws ecs update-service --service fronted"
                sh "aws ecs update-service --service backend --cluster test-project"
                sh "aws ecs update-service --service frontend --cluster test-project"
            }
        }
    }
}