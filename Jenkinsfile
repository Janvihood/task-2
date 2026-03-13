pipeline {
    agent any

    environment {
        // Set paths to tools inside Jenkins container
        SONAR_SCANNER = "/opt/sonar-scanner/bin/sonar-scanner"
        DEP_CHECK    = "/opt/dependency-check/bin/dependency-check.sh"
        REPORTS_DIR  = "reports"
        SONAR_TOKEN  = "squ_4fcc7688de74566c4c8b90cece08171b73dd17b9" // replace if needed
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: 'https://github.com/Janvihood/task-2.git']]])
            }
        }

        stage('Create Reports Folder') {
            steps {
                sh "mkdir -p ${REPORTS_DIR}"
            }
        }

        stage('SAST Scan') {
            steps {
                sh "${SONAR_SCANNER} -Dsonar.projectKey=SecureApp -Dsonar.host.url=http://sonarqube:9000 -Dsonar.login=${SONAR_TOKEN}"
            }
        }

        stage('Dependency Scan') {
            steps {
                sh "${DEP_CHECK} --scan . --format HTML -o ${REPORTS_DIR}"
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t secureapp:latest .'
            }
        }

        stage('Image Scan') {
            steps {
                sh 'trivy fs --security-checks vuln .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: "${REPORTS_DIR}/*", allowEmptyArchive: true
            echo "Build and scans finished! Check reports in Jenkins."
        }
        failure {
            echo "Pipeline failed. Check logs for errors."
        }
    }
}
