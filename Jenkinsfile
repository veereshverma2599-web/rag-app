pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "rag-app"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                sh '''
                echo "Stopping existing containers..."
                cd infra
                docker compose down || true

                echo "Building Docker images..."
                docker compose build
                '''
            }
        }

        stage('Start Containers') {
            steps {
                sh '''
                echo "Starting containers..."
                cd infra
                docker compose up -d
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                echo "Checking running containers..."
                docker ps
                '''
            }
        }

    }

    post {

        success {
            echo 'Deployment Successful 🚀'
        }

        failure {
            echo 'Build Failed ❌'
        }

        always {
            echo 'Pipeline Finished.'
        }
    }
}
