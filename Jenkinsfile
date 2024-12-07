pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '82abd174-f0b0-4952-aa01-145210e3766a', url: 'https://github.com/mletre/testingjenkins.git']])
            }
        }
    }
}
