pipeline {
    agent any

    environment {
        IMAGE_NAME = "secure-app"
        SONAR_HOST = "http://localhost:9000"
        SONAR_TOKEN = "squ_47204c751b4eaec36289ff40daa19004811c7bc2"
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
           
            /opt/sonar-scanner/bin/sonar-scanner \
            -Dsonar.projectKey=task-2 \
            -Dsonar.projectName=task-2 \
            -Dsonar.sources=. \
            -Dsonar.inclusions=**/*.py \
            -Dsonar.host.url=http://sonarqube:9000 \
            -Dsonar.login=$SONAR_TOKEN
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
                 aquasec/trivy image $IMAGE_NAME:latest
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
                echo "Deploying..."

                export KUBECONFIG=/var/jenkins_home/.kube/config

                echo "Using kubeconfig:"
                kubectl config view | grep server

                kubectl get nodes

                kubectl apply -f deployment.yaml
                kubectl apply -f service.yaml
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
