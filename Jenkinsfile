pipeline {
    agent any

    stages {

        stage('Build Docker Images') {
            steps {
                sh '''
                cd infra
                docker-compose down || true
                docker-compose build
                '''
            }
        }

        stage('Start Containers') {
            steps {
                sh '''
                cd infra
                docker-compose up -d
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
    }
}

