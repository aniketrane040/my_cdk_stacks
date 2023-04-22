pipeline {
    agent any 
    environment {
        AWS_DEFAULT_REGION = 'us-east-1'
    }
    stages {
        stage('Welcome') {
            steps {
                echo 'Hello Aniket !'
            }
        }

        stage('Install Dependencies') {
          steps {
            sh 'pip install -r requirements.txt'
          }
        }

        stage('Unit Testing') {
          steps {
            withAWS(role: 'arn:aws:iam::402310761567:role/cdk-deploy') {
              sh 'python -m unittest discover -v'
            }
          }
        }

        stage('Deply cdk Stack') {
            steps {
                sh 'cdk synth'
                sh 'cdk diff'
                sh 'cdk deploy'
            }
        }

        stage('Done') {
            steps {
                echo 'done !'
            }
        }
    }
    
}
