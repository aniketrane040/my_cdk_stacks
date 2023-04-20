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
            withAWS(region: 'us-east-1', role: 'arn:aws:iam::402310761567:role/cdk-deploy')
            steps {
                sh 'cdk synth'
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
