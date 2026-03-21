pipeline {
    agent any

    environment {
        IMAGE_NAME = "secure-app"
        SONAR_HOST = "http://localhost:9000"
        SONAR_TOKEN = "squ_44bfb9d597524e9fedfc9b576e5c69ff9a6a046d"
    }


        stage('SonarQube Scan') {
            steps {
                 sh '''
        docker run --rm --network host \
        -v $(pwd):/usr/src \
        -v sonar_cache:/opt/sonar-scanner/.sonar \
        -w /usr/src \
        -e SONAR_SCANNER_OPTS="-Xmx512m" \
        sonarsource/sonar-scanner-cli \
        -Dsonar.host.url=${SONAR_HOST} \
        -Dsonar.token=${SONAR_TOKEN}
        '''
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

        stage('Deploy to Kubernetes') {
            steps {
                sh """
                docker run --rm \
                -v \root/.kube:/root/.kube \
                -v \$(pwd):/workspace \
                bitnami/kubectl \
                kubectl apply -f /workspace/deployment.yaml
                """
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
