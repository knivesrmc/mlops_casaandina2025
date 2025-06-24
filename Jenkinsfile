pipeline{
    agent any

    environment {
        VENV_DIR = 'venv'
        
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
        stage('Setting up our Virtual Environment and Installing dependancies'){
            steps{
                script{
                    echo 'Setting up our Virtual Environment and Installing dependancies............'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }
    }
   
}