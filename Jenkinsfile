pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "secure-app"
        SONAR_TOKEN = "squ_a4191dddd07437c399fcc0be16bf985c45d110e1"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Janvihood/task-2.git'
            }
        }

        stage('SAST Scan') {
            steps {
                sh '''
                sonar-scanner \
                -Dsonar.projectKey=SecureApp \
                -Dsonar.host.url=http://localhost:9000 \
                -Dsonar.login=$SONAR_TOKEN
                '''
            }
        }

        stage('Dependency Scan') {
            steps {
                sh '''
                dependency-check/bin/dependency-check.sh \
                --scan . \
                --format HTML
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Image Scan') {
            steps {
                sh "trivy image ${DOCKER_IMAGE}"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh "kind load docker-image ${DOCKER_IMAGE} --name devsecops-cluster"
                sh "kubectl apply -f deployment.yaml"
                sh "kubectl apply -f service.yaml"
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/dependency-check-report.html', allowEmptyArchive: true
        }
        success {
            echo "Pipeline finished successfully!"
        }
        failure {
            echo "Pipeline failed, check logs!"
        }
    }
}
