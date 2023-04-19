pipeline {
    agent any 
        
    stages {
        stage('Hello World') {
            steps {
                echo 'Hello Aniket !'
            }
        }

        stage('Assume role') {
            steps {
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'assumed_role'
                    accessKeyVariable: 'AWS_ACCESS_KEY_ID'
                    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                ]]) {   
                    sh 'aws s3 ls'
                    sh 'aws sts get-caller-identity'
                }
            }
        }

        stage('Done') {
            echo 'done !'
        }
    }
    
}
