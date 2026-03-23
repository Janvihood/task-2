pipeline {
    agent any

    environment {
        IMAGE_NAME = "secure-app"
        SONAR_HOST = "http://localhost:9000"
        SONAR_TOKEN = "squ_44bfb9d597524e9fedfc9b576e5c69ff9a6a046d"
        DEPLOYMENT_FILE = "deployment.yaml"
        PATH = "/usr/local/bin:${env.PATH}"
        KUBECONFIG = "/var/jenkins_home/kubeconfig"
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
         }


        stage('Check Docker') {
            steps {
                sh 'docker --version'
           }
        }

        stage('Debug Files') {
           steps {
               sh '''
               echo "Current directory:"
               pwd
               echo "Files:"
               ls -la
               '''
           }
        }

        stage('SonarQube Scan') {
            steps {
           sh '''
            echo "========== DEBUG START =========="
            echo "Workspace: $WORKSPACE"

            echo "Files in workspace:"
            ls -la $WORKSPACE

            echo "Python files:"
            find $WORKSPACE -name "*.py"

            echo "========== VERIFY INSIDE DOCKER =========="
            docker run --rm --network host \
            -v $WORKSPACE:/usr/src \
            alpine sh -c "echo 'Inside container:' && ls -la /usr/src && find /usr/src -name '*.py'"

            echo "========== RUNNING SONAR =========="
            docker run --rm --network host \
            -v $WORKSPACE:/usr/src \
            -v sonar_cache:/opt/sonar-scanner/.sonar \
            -w /usr/src \
            sonarsource/sonar-scanner-cli \
            -Dsonar.projectKey=task-2 \
            -Dsonar.projectName=task-2 \
            -Dsonar.sources=. \
            -Dsonar.host.url=http://localhost:9000 \
            -Dsonar.token=$SONAR_TOKEN
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
                if [ ! -f kubectl ];
                then
                  echo "Installing kubectl..."
                  curl -LO https://dl.k8s.io/release/v1.29.0/bin/linux/amd64/kubectl
                  chmod +x kubectl
                  
                fi
                export KUBECONFIG=/var/jenkins_home/kubeconfig
                kubectl get nodes
                kubectl apply -f deployment.yaml  
            
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
