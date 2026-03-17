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
        docker run --rm \
        --network host \
        -e SONAR_HOST_URL="http://localhost:9000" \
        -e SONAR_TOKEN="squ_7fe703de969819b0b6ac084e230ecffb24578ffb" \
        -v $(pwd):/usr/src \
        sonarsource/sonar-scanner-cli
        -Dsonar.projectKey=task-2 \
        -Dsonar.sources=.
        '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t secure-app .'
            }
        }

        stage('Trivy Security Scan') {
             steps {
                  sh '''
                  docker run --rm \
                  -v $(pwd):/project \
                  aquasec/trivy fs /project || true
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
