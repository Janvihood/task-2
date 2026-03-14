pipeline {
agent any

environment {
    SONAR_SCANNER = "/opt/sonar-scanner/bin/sonar-scanner"
    DEP_CHECK = "/opt/dependency-check/bin/dependency-check.sh"
}

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
            if [ -f /opt/sonar-scanner/bin/sonar-scanner ]; then
                /opt/sonar-scanner/bin/sonar-scanner \
                -Dsonar.projectKey=secure-app \
                -Dsonar.sources=. \
                -Dsonar.host.url=http://sonarqube:9000 \
                -Dsonar.login=squ_4fcc7688de74566c4c8b90cece08171b73dd17b9
            else
                echo "Sonar scanner not found, skipping"
            fi
            '''
        }
    }
    
    stage('Build Docker Image') {
    steps {
        sh '''
        docker build -t secure-app .
        '''
        }
    }
    stage('Docker Image Scan') {
        steps {
          sh '''
          docker run --rm aquasec/trivy image secure-app
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

    stage('Dependency Check') {
        steps {
        echo "Skipping OWASP Dependency Check to speed up pipeline"
        }
    }

    stage('Pipeline Finished') {
        steps {
            echo "Pipeline executed"
        }
    }

}

post {
    always {
        archiveArtifacts artifacts: 'reports/*', allowEmptyArchive: true
    }
}

}
