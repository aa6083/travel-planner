pipeline {
    agent any
    environment {
        DOCKERHUB_USER = 'affanalrayyan'
        IMAGE_NAME = 'travel-planner'
    }
    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/aa6083/travel-planner.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat "docker build -t %DOCKERHUB_USER%/%IMAGE_NAME%:latest ."
            }
        }
        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', 
                                usernameVariable: 'USERNAME', 
                                passwordVariable: 'PASSWORD')]) {
                    bat "docker login -u %USERNAME% -p %PASSWORD%"
                    bat "docker push %DOCKERHUB_USER%/%IMAGE_NAME%:latest"
                }
            }
        }
        stage('Done') {
            steps {
                echo 'Travel Planner deployed successfully!'
            }
        }
    }
}