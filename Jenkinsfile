pipeline {
    agent any

    environment {
        IMAGE_NAME = "secure-app"
        SONAR_HOST = "http://localhost:9000"
        SONAR_TOKEN = "squ_44bfb9d597524e9fedfc9b576e5c69ff9a6a046d"
        DEPLOYMENT_FILE = "deployment.yaml"
        PATH = "/usr/local/bin:${env.PATH}"
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
                aquasec/trivy image $IMAGE_NAME
                '''
            }
        }

        stage('Debug Environment') {
            steps {
                sh '''
                echo "PATH=$PATH"
                which kubectl || echo "kubectl NOT FOUND"
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                # Install kubectl if missing
                if ! command -v kubectl >/dev/null 2>&1
                then
                  echo "Installing kubectl..."
                  curl -LO https://dl.k8s.io/release/v1.29.0/bin/linux/amd64/kubectl
                  chmod +x kubectl
                  
                fi

                ./kubectl version --client
                ./kubectl apply -f ${DEPLOYMENT_FILE} --validate=false
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
