pipeline {
    agent any 
    environment {
        AWS_REGION = 'us-east-1'
        AWS_ACCOUNT_ID = '402310761567'
    }
    stages {
        stage('Hello World') {
            steps {
                echo 'Hello Aniket !'
            }
        }

        stage('Assume role') {
            steps {
                withCredentials([
                    [
                        $class: 'AmazonWebServicesCredentialsBinding',
                        accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                        secretKeyVariable: 'AWS_SECRET_ACCESS_KEY',
                        credentialsId: 'my-aws-creds'
                    ]
                ]) {
                    sh 'aws s3 ls'
                    sh 'aws sts get-caller-identity'
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
