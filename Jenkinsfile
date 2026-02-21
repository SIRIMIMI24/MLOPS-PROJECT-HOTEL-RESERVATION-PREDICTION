pipeline{
    agent any

    environment {
        VENV_DIR = 'venv'
    }
    
    stages{
        stage('Cloning Githup Repository to Jenkins'){
            steps{
                script{
                    echo 'Cloning Githup Repository to Jenkins .........'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'githup-token', url: 'https://github.com/SIRIMIMI24/MLOPS-PROJECT-HOTEL-RESERVATION-PREDICTION.git']])
                }
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