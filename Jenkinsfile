pipeline{
    agent any

    environment {
        VENV_DIR = 'venv'
        IMAGE_NAME = 'hotel-reservation-model'
    }

    stages{

        stage('Clone Repository'){
            steps{
                checkout scm
            }
        }

        stage('Setup Virtual Environment'){
            steps{
                sh '''
                python -m venv ${VENV_DIR}
                . ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install -e .
                '''
            }
        }

        stage('Train Model'){
            steps{
                sh '''
                . ${VENV_DIR}/bin/activate
                python pipeline/training_pipeline.py
                '''
            }
        }

        stage('Build Docker Image'){
            steps{
                sh '''
                docker build -t ${IMAGE_NAME}:latest .
                '''
            }
        }

        stage('Deploy Locally'){
            steps{
                sh '''
                docker stop hotel-container || true
                docker rm hotel-container || true
                docker run -d \
                -p 5000:5000 \
                --name hotel-container \
                ${IMAGE_NAME}:latest
                '''
            }
        }
    }
}