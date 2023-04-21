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
    stage('Check SSM Parameter') {
            steps {
                script {
                    stackName = 'MyCdkStackNew'
                    paramName1 = 'parameter_name'
                    def paramName = sh(
                              returnStdout: true,
                              script: "python my_cdk_stack/my_cdk_stack_stack.py get_param_value ${stackName} ${paramName1}"
                          ).trim()
                //    def paramName = "/cre/ami-id"
                    def paramValue = sh(returnStdout: true, script: "aws ssm get-parameter --name ${paramName} --query 'Parameter.Value' --output text")
                    if (paramValue) {
                        echo "SSM parameter ${paramName} has a value: ${paramValue}"
                    } else {
                        error "SSM parameter ${paramName} does not exist or has no value."
                    }
                }
            }
    }
    stage('Deploy') {
        steps {
          script{
              withAWS(region: 'us-east-1', role: 'arn:aws:iam::402310761567:role/cdk-deploy') {
              sh 'cdk synth'
              sh 'cdk diff'
              sh 'cdk synth'
              sh 'cdk deploy --require-approval never'
              }
            }
        }
    }

  }
}
