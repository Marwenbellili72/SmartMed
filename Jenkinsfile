pipeline {
    agent any

    environment {
        SONAR_SCANNER_HOME = tool 'SonarQube Scanner'
        IMAGE_NAME_NGINX = "marwenbellili/nginx"
        IMAGE_NAME_SMARTMED = "marwenbellili/smartmed"
        TAG = "latest"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Marwenbellili72/SmartMed.git'
                sh 'ls -la'  
            }
        }

        stage('SonarQube Scan') {
            steps {
                script {
                    echo "Lancement du scan SonarQube..."
                    withSonarQubeEnv('SonarQube Server') { 
                        sh "${SONAR_SCANNER_HOME}/bin/sonar-scanner \
                            -Dsonar.host.url=http://172.28.96.1:9000 \
                            -Dsonar.projectKey=SmartMed"
                    }
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    echo "Construction des images Docker..."
                    sh 'ls -R'  
                    sh "docker build -t ${IMAGE_NAME_NGINX}:${TAG} -f nginx/Dockerfile nginx"
                    sh "docker build -t ${IMAGE_NAME_SMARTMED}:${TAG} -f SmartMed/Dockerfile SmartMed"
                }
            }
        }

        stage('Security Scan with Trivy') {
            steps {
                script {
                    echo "Analyse de sécurité des images Docker avec Trivy..."
                    sh "trivy image ${IMAGE_NAME_NGINX}:${TAG}"
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    echo "Publication des images sur Docker Hub..."
                    withCredentials([string(credentialsId: 'docker_hub_token', variable: 'DOCKER_HUB_TOKEN')]) {
                        sh "echo ${DOCKER_HUB_TOKEN} | docker login -u marwenbellili --password-stdin"
                        sh "docker push ${IMAGE_NAME_NGINX}:${TAG}"
                        sh "docker push ${IMAGE_NAME_SMARTMED}:${TAG}"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo "Déploiement..."
                    sh "docker-compose up -d"
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
