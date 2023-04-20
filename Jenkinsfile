pipeline {
  agent any
  environment {
    AWS_DEFAULT_REGION = 'us-east-1'
    AWS_DEFAULT_OUTPUT = 'json'
  }
  stages {
    stage('Checkout') {
      steps {
        checkout([$class: 'GitSCM',
                  branches: [[name: '*/develop']],
                  userRemoteConfigs: [[url: 'https://github.com/aniketrane040/my_cdk_stacks.git']]])
      }
    }
    stage('Build') {
      steps {
        sh 'sudo yum install npm -y'
        sh 'npm install aws-cdk'
        sh 'npm install'
        sh 'npm run build'
      }
    }
    stage('Deploy') {
        steps {
            withAWS(region: 'us-east-1', role: 'arn:aws:iam::402310761567:role/jenkins-cf') {
            sh 'npm run cdk -- deploy --require-approval never'
            }
        }
    }

  }
}
