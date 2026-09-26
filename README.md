DevSecOps CI/CD Project

A containerized Python application demonstrating a DevSecOps-oriented CI/CD pipeline using Docker, Jenkins, SonarQube, Trivy, and Kubernetes.

🚀 Project Overview

This project automates the process of building, scanning, and deploying a Python application using modern DevOps and DevSecOps practices.

The pipeline is designed to cover:

Source code integration with Git/GitHub

Docker image creation

Continuous Integration with Jenkins

Static code analysis with SonarQube

Container vulnerability scanning with Trivy

Kubernetes deployment

Application service exposure

Application metrics for monitoring

🛠️ Technologies Used

Technology

Purpose

Python / Flask

Application development

Docker

Containerization

Jenkins

CI/CD automation

SonarQube

Static code quality analysis

Trivy

Container vulnerability scanning

Kubernetes

Application orchestration

Git / GitHub

Source-code management

Prometheus-compatible metrics

Application monitoring

📁 Project Structure

task-2/
├── .dockerignore
├── Dockerfile
├── Dockerfile.jenkins
├── Jenkinsfile
├── app.py
├── deployment.yaml
├── kubeconfig
├── requirements.txt
├── service.yaml
├── sonar-project.properties
└── trivy_0.69.3_Linux-64bit.deb

File Description

app.py – Python application and application metrics.

requirements.txt – Python dependencies.

Dockerfile – Builds the application container image.

Dockerfile.jenkins – Docker environment used for Jenkins-related pipeline execution.

Jenkinsfile – Defines the CI/CD pipeline stages.

sonar-project.properties – SonarQube project configuration.

deployment.yaml – Kubernetes Deployment configuration.

service.yaml – Kubernetes Service configuration.

.dockerignore – Prevents unnecessary files from being copied into the Docker image.

kubeconfig – Kubernetes cluster configuration used by the deployment workflow.

trivy_0.69.3_Linux-64bit.deb – Trivy package included for vulnerability scanning.

🔄 CI/CD Pipeline

The project follows a workflow similar to:

Developer
   │
   ▼
GitHub Repository
   │
   ▼
Jenkins
   │
   ├── Checkout Source Code
   │
   ├── Build Application
   │
   ├── SonarQube Code Analysis
   │
   ├── Docker Image Build
   │
   ├── Trivy Security Scan
   │
   ▼
Kubernetes Deployment
   │
   ├── Deployment
   └── Service
   │
   ▼
Running Application

🔐 DevSecOps Practices

Security is integrated into the CI/CD workflow instead of being treated as a separate final step.

SonarQube

SonarQube is used for static analysis to identify code-quality issues and potential bugs in the application source code.

Trivy

Trivy is used to scan the container image for known vulnerabilities before deployment.

This helps identify vulnerable packages and dependencies that could introduce security risks.

☸️ Kubernetes Deployment

The application is deployed to Kubernetes using:

deployment.yaml for application Pods and deployment configuration.

service.yaml for exposing the application through a Kubernetes Service.

Example deployment flow:

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

Check the deployment:

kubectl get deployments
kubectl get pods
kubectl get services

🐳 Docker

Build the application image:

docker build -t devsecops-app .

Run the container:

docker run -p 5000:5000 devsecops-app

The port can be changed according to the port configured in app.py and the Docker/Kubernetes configuration.

🔍 Security Scanning

A typical Trivy scan can be performed with:

trivy image devsecops-app

The scan can be used to identify vulnerabilities in operating-system packages and application dependencies contained in the image.

📊 Monitoring

The application contains metrics functionality in app.py, which can be used as a foundation for monitoring application behavior.

This can be integrated with a Prometheus/Grafana monitoring stack for dashboards and observability.

▶️ Running the Project Locally

1. Clone the repository

git clone <YOUR_GITHUB_REPOSITORY_URL>
cd task-2

2. Install dependencies

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. Run the application

python app.py

4. Build the Docker image

docker build -t devsecops-app .

5. Run the container

docker run -p 5000:5000 devsecops-app

🎯 Key DevOps Concepts Demonstrated

CI/CD pipeline automation

Infrastructure/application deployment with Kubernetes

Containerization using Docker

Static code analysis

Container security scanning

Git-based development workflow

Application metrics and observability

Security integrated into the software delivery lifecycle

💼 Resume Description

DevSecOps CI/CD Pipeline | Docker, Jenkins, Kubernetes, SonarQube, Trivy

Built a DevSecOps CI/CD pipeline for a Python application using Jenkins, Docker, Kubernetes, SonarQube, and Trivy. Automated application build and deployment workflows, integrated static code analysis and container vulnerability scanning, and configured Kubernetes Deployment/Service manifests with application metrics for monitoring.

📌 Future Enhancements

Add Docker image publishing to Docker Hub/Amazon ECR.

Add Kubernetes Secrets and ConfigMaps.

Integrate Prometheus and Grafana dashboards.

Add OWASP Dependency-Check to the security pipeline.

Add automated rollback on failed deployments.

Add Kubernetes RBAC and network policies.

Add automated testing before deployment.

👩‍💻 Author

Janvi Hood

B.Tech Computer Engineering | CDAC DITISS

Interested in DevOps, Cloud, AWS, Linux, Kubernetes, and DevSecOps.
