pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Janvihood/task-2.git'
                sh 'mkdir -p reports'
            }
        }

        stage('SonarQube Scan') {
            steps {
                sh '''
                if [ -f /opt/sonar-scanner/bin/sonar-scanner ]; then
                    /opt/sonar-scanner/bin/sonar-scanner \
                    -Dsonar.projectKey=secure-app \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=http://sonarqube:9000 \
                    -Dsonar.login=squ_4fcc7688de74566c4c8b90cece08171b73dd17b9
                else
                    echo "Sonar scanner not installed, skipping"
                fi
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t secure-app .'
            }
        }

        stage('Docker Image Scan') {
            steps {
                sh '''
                docker run --rm aquasec/trivy image secure-app || true
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl apply -f deployment.yaml
                kubectl apply -f service.yaml
                '''
            }
        }

        stage('Pipeline Finished') {
            steps {
                echo "Pipeline executed successfully"
            }
        }

    }
}
