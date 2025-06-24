pipeline{
    agent any

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = "mlops-new-447207"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
    }

    stages{
        stage('Clonando repositorio Github en Jenkins'){
            steps{
                script{
                    echo 'Clonando la repo............'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/knivesrmc/mlops_casaandina2025.git']])
                }
            }
        }
}
}