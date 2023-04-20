pipeline {
    agent any 
    environment {
        AWS_DEFAULT_REGION = 'us-east-1'
        ROLE_ARN = 'arn:aws:iam::402310761567:role/jenkins_role'
    }
    stages {
        stage('Hello World') {
            steps {
                echo 'Hello Aniket !'
            }
        }

        stage('Assume role') {
            steps {
                withAWS(role: 'arn:aws:iam::402310761567:role/jenkins_role') {
                    sh 'cdk deploy MyCDkStack'
                }
            }
        }

        stage('Done') {
            steps {
                echo 'done !'
            }
        }
    }
    
}
