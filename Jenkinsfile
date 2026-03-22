pipeline {
    agent any

    environment {
        IMAGE_NAME = "secure-app"
        SONAR_HOST = "http://localhost:9000"
        SONAR_TOKEN = "squ_44bfb9d597524e9fedfc9b576e5c69ff9a6a046d"
    }

    stages {

        stage('SonarQube Scan') {
            steps {
                 sh """
        docker run --rm --network host \
        -v \$(pwd):/usr/src \
        -v sonar_cache:/opt/sonar-scanner/.sonar \
        -w /usr/src \
        sonarsource/sonar-scanner-cli \
        -Dsonar.projectKey=task-2 \
        -Dsonar.projectName=task-2 \
        -Dsonar.sources=/usr/src \
        -Dsonar.host.url=${SONAR_HOST} \
        -Dsonar.login=${SONAR_TOKEN}
        """
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Trivy Image Scan') {
            steps {
                sh '''
                docker run --rm \
                -v /var/run/docker.sock:/var/run/docker.sock \
                -v trivy_cache:/root/.cache/trivy \
                aquasec/trivy image secure-app
                '''
            }
        }

        stage('Debug Workspace') {
            steps {
                sh 'pwd && ls -la'
            }
        }

	stage('Deploy to Kubernetes') {
            steps {
                sh '''
        docker run --rm \
        --volumes-from jenkins \
        -v /root/.kube:/root/.kube \
        bitnami/kubectl \
        kubectl apply -f /var/jenkins_home/workspace/task-2/deployment.yaml
        '''
            }
        }
    }

    post {
        always {
            echo "Pipeline completed."
        }
        success {
            echo "SUCCESS 🚀"
        }
        failure {
            echo "FAILED ❌"
        }
    }
}
