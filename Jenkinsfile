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
