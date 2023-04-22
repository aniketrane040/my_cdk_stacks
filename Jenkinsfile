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

        // stage('Unit Testing') {
        //   steps {
        //     sh 'python tests/unit/test_my_cdk_stack_stack.py'
        //   }
        // }

        stage('Deply cdk Stack') {
            steps {
                sh 'cdk synth'
                sh 'cdk deploy --require-approval never'
            }
        }

        stage('Done') {
            steps {
                echo 'done !'
            }
        }
    }
    
}
