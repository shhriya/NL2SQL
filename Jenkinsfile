pipeline {
    agent any

    environment {
        PROJECT_DIR = '/var/jenkins_home/workspace/nl2sql-ci-cd'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from Git repository
                git 'https://github.com/shhriya/nl2sql.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    // Build the Docker image for your project
                    sh 'docker build -t nl2sql-app .'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run tests or validations
                    sh 'docker run --rm nl2sql-app pytest'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Deploy your application (e.g., start the app on a cloud server or Docker)
                    sh 'docker run -d -p 5000:5000 nl2sql-app'
                }
            }
        }
    }

    post {
        always {
            // Clean up Docker containers
            sh 'docker system prune -f'
        }
    }
}
