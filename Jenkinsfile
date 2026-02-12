pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-ssh',
                    url: 'git@github.com:veereshverma2599-web/rag-app.git'
            }
        }

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
