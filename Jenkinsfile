pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'affanalrayyan'
        IMAGE_NAME     = 'travel-planner'
    }

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/aa6083/travel-planner.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build --no-cache -t %DOCKERHUB_USER%/%IMAGE_NAME%:latest .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    bat 'docker login -u %DOCKER_USER% -p %DOCKER_PASS%'
                    bat 'docker push %DOCKERHUB_USER%/%IMAGE_NAME%:latest'
                }
            }
        }

        stage('Done') {
            steps {
                echo '✅ Image pushed to DockerHub!'
                echo 'Now restart container on EC2 manually'
            }
        }
    }
}