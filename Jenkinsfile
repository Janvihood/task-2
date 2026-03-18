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
        docker run --rm --network host \
        -v /var/jenkins_home/workspace/task-2:/usr/src \
        -w /usr/src \
        sonarsource/sonar-scanner-cli \
        -Dsonar.projectKey=task-2 \
        -Dsonar.sources=. \
        -Dsonar.host.url=http://localhost:9000 \
        -Dsonar.login=squ_44bfb9d597524e9fedfc9b576e5c69ff9a6a046d
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
