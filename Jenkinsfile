pipeline{
    agent any
    
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
}