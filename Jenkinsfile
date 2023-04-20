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
    stage('Deploy') {
        steps {
            withAWS(region: 'us-east-1', role: 'arn:aws:iam::402310761567:role/cdk-deploy') {
            sh 'cdk synth'
            sh 'cdk deploy --verbose "test-ec2-jenkins" --require-approval never --role-arn arn:aws:iam::402310761567:role/jenkins-cf'
            }
        }
    }

  }
}
