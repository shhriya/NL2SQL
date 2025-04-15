pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    // Run your build commands (e.g., Docker build)
                    sh 'docker build -t my-jenkins .'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run your tests here
                    sh 'python -m unittest discover'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Add your deployment steps here
                    sh 'docker run -d -p 8080:8080 my-jenkins'
                }
            }
        }
    }
}
