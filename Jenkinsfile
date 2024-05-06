pipeline {
    environment {
        registry = "aymanazzam63/app"
        KUBECONFIG = credentials('k8s_config')
    }
    agent any
    parameters {
        string(name: 'IMAGE_TAG', defaultValue: '1.0', description: 'Image tag like 1.0 or 2.0, ...etc')
    }
    stages {
        stage('Deploy the image into the cluster deployment') {
            steps{
                dir('./helm/app'){
                    powershell "gcloud components install gke-gcloud-auth-plugin"
                    powershell "kubectl config set-context minikube --namespace=development"
                    powershell "helm upgrade --set imageTag=${params.IMAGE_TAG} app ."
                }
            }
        }
    }
}