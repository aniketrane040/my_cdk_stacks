pipeline {
    agent any 
    environment {
        AWS_DEFAULT_REGION = 'us-east-1'
        ROLE_ARN = 'arn:aws:iam::402310761567:role/MyCdkStackStack-InstanceInstanceRoleE9785DE5-1A10IOOHKJ0WJ'
    }
    stages {
        stage('Hello World') {
            steps {
                echo 'Hello Aniket !'
            }
        }

        stage('Assume role') {
            steps {
                sh 'cdk synth'
                sh 'cdk deploy MyCDkStack'
            }
        }

        stage('Done') {
            steps {
                echo 'done !'
            }
        }
    }
    
}
