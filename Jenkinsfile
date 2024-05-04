pipeline {
    environment {
        registry = "aymanazzam63/app"
        registryCredential = 'dockerhub_user'
        dockerImage = ''
    }
    agent any
    stages {
        stage('Building the image') {
            steps{
                script {
                    dockerImage = docker.build(registry + ":" + currentBuild.number)
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
        stage('Invoke deployment pipeline') {
            steps{
                build job: 'isolution - Deployment', parameters: [string(name: 'IMAGE_TAG', value: "${currentBuild.number}")], wait: false
            }
        }
    }
}