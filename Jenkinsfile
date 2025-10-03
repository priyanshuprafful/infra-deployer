pipeline {
    agent any
    environment {
        DOCKERHUB = credentials('dockerhub-creds-id')
        IMAGE = 'priyanshuprafful/infra-deployer'
        CONTAINER_NAME = 'infra-deployer'
        APP_PORT = '5000'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/priyanshuprafful/infra-deployer.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE}:latest .'
            }
        }

        stage('Docker Login & Push') {
            steps {
                sh 'echo $DOCKERHUB_PSW | docker login -u $DOCKERHUB_USR --password-stdin'
                sh 'docker push ${IMAGE}:latest'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
            docker rm -f infra-deployer || true
            if [ "$(docker ps -aq --filter 'ancestor=${IMAGE}:latest')" ]; then
                docker stop $(docker ps -aq --filter 'ancestor=${IMAGE}:latest')
                docker rm $(docker ps -aq --filter 'ancestor=${IMAGE}:latest')
            fi
            docker run -d --name infra-deployer -p ${APP_PORT}:${APP_PORT} ${IMAGE}:latest
        '''
            }
        }
    }
}