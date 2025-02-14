pipeline {
    agent any

    environment {
        PYTHON_ENV = 'python3.12'
    }

    stages {
        stage('Install dependencies') {
            steps {
                script {
                    bat 'pip install -r requirements.txt'
                }
            }
        }
        
        stage('Run tests') {
            steps {
                script {
                    bat 'python -m pytest tests_spotify.py'
                }
            }
        }

        stage('Evaluate code quality') {
            steps {
                script {
                    bat 'python evaluar_calidad.py'
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
