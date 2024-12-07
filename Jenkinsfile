pipeline {
    agent any

    environment {
        GCP_PROJECT = 'datalabs-hs'
        REPO_LOCATION = 'asia-southeast2'
        GCP_REPO_NAME = 'jenkinsrepo'
    }

    stages {
        stage('Hello') {
            steps {
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '82abd174-f0b0-4952-aa01-145210e3766a', url: 'https://github.com/mletre/testingjenkins.git']])
            }
        }
        stage('Build Back-End Image') {
            steps {
                script {
                    def appDockerfile = 'backend/Dockerfile'
                    def IMAGE_NAME = "${REPO_LOCATION}-docker.pkg.dev/${GCP_PROJECT}/${GCP_REPO_NAME}/testingimage"
                    docker.build "${IMAGE_NAME}:latest", "-f ${appDockerfile} ."
                }
            }
        }

        stage('Push Back-End Image') {
            steps {
                script {
                    def IMAGE_NAME = "${REPO_LOCATION}-docker.pkg.dev/${GCP_PROJECT}/${GCP_REPO_NAME}/testingimage"
                    withCredentials([file(credentialsId: 'adb3414c-5c36-410c-9943-ebd0151b9809', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                        sh 'cat "${GOOGLE_APPLICATION_CREDENTIALS}" | docker login -u _json_key --password-stdin https://"${REPO_LOCATION}"-docker.pkg.dev'
                        sh "docker push ${IMAGE_NAME}:latest"
                        sh 'docker logout https://"${REPO_LOCATION}"-docker.pkg.dev'
                    }
                }
            }
        }
    }

}
