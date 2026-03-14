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
        -e SONAR_HOST_URL="http://host.docker.internal:9000" \
        -e SONAR_LOGIN="squ_4fcc7688de74566c4c8b90cece08171b73dd17b9" \
        -v $(pwd):/usr/src \
        sonarsource/sonar-scanner-cli
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
