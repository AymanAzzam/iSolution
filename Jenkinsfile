pipeline {
    environment {
        registry = "aymanazzam63/app"
        registryCredential = 'dockerhub_user'
        dockerImage = ''
        KUBECONFIG = credentials('k8s_config')
    }
    agent any
    parameters {
        string(name: 'IMAGE_TAG', defaultValue: '1.0', description: 'Image tag like 1.0 or 2.0, ...etc')
    }
    stages {
        stage('Building the image') {
            steps{
                dir('./App/'){
                    script {
                        dockerImage = docker.build(registry + ":${params.IMAGE_TAG}")
                    }
                }
            }
        }
        stage('Upload the image to docker hub') {
            steps{
                script {
                        docker.withRegistry('', registryCredential ) {
                            dockerImage.push()
                        }
                }
            }
        }
        stage('Deploy the image into the cluster deployment') {
            steps{
                dir('./helm/app'){
                    powershell "kubectl config set-context minikube --namespace=development"
                    powershell "helm upgrade --set imageTag=${params.IMAGE_TAG} app ."
                }
            }
        }
        stage('Cleaning up') {
            steps{
                powershell "docker rmi $registry:${params.IMAGE_TAG}"
            }
        }
    }
}