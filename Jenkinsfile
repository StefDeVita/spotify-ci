pipeline {
    agent any
	
	triggers {
        githubPush()
    }

    environment {
        PYTHON_ENV = 'python3.12'
        GENIUS_ACCESS_TOKEN = '8PwekH6DC_sPYD1qpblw1rwUAl6HXj_yOSqviVeyWB5-3VcgR7frBwYqEqaw8t8f'
    }

    stages {
		stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/StefDeVita/spotify-ci.git'
            }
        }

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
                    bat 'python metricas_calidad.py'
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
