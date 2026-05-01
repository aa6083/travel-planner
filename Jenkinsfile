pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'affanalrayyan'
        IMAGE_NAME     = 'travel-planner'
        AWS_KEY        = 'projectkey'
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

        stage('Terraform Init & Apply') {
            steps {
                withCredentials([
                    string(credentialsId: 'aws-access-key', variable: 'AWS_ACCESS_KEY_ID'),
                    string(credentialsId: 'aws-secret-key', variable: 'AWS_SECRET_ACCESS_KEY')
                ]) {
                    dir('terraform') {
                        bat 'terraform init'
                        bat 'terraform apply -auto-approve -var="key_name=%AWS_KEY%"'
                    }
                }
            }
        }

        stage('Done') {
            steps {
                dir('terraform') {
                    bat 'terraform output app_url'
                }
                echo '✅ Travel Planner is LIVE on AWS!'
            }
        }
    }
}