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
                    script {
                        env.DB_USERNAME = powershell(returnStatus: true, script: "vault kv get -mount=secret -field=username db")
                    }
                    script {
                        env.DB_PASSWORD = powershell(returnStatus: true, script: "vault kv get -mount=secret -field=password db")
                    }
                    powershell "kubectl config set-context minikube --namespace=development"
                    powershell "helm upgrade --set imageTag=${params.IMAGE_TAG} --set dbUsername=$env:DB_USERNAME --set dbPassword=$env:DB_PASSWORD app ."
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