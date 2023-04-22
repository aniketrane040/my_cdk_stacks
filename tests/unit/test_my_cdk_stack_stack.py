import aws_cdk as core
import unittest
import aws_cdk.assertions as assertions
import boto3
# from aws_cdk import (
#     aws_ssm as ssm
# )
# from my_cdk_stack.my_cdk_stack_stack import MyCdkStackStack

# class TestMyStack(unittest.TestCase):

#     def test_ssm_parameter(self):
#         app = core.App()
#         stack = MyCdkStackStack(app, "test-stack",env=env_USA)

#         Retrieve the parameter value from SSM Parameter Store
#         parameter_name = '/cre/ami-id'
#         parameter_value = ssm.StringParameter.value_for_string_parameter(
#             stack, 
#             parameter_name=parameter_name
#         )

#         Check that the parameter value is correct
#         self.assertEqual(parameter_value, "ami-06e46074ae430fba6")

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_cdk/aws_cdk_stack.py
class TestSSMParameter(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.session = boto3.Session()
        self.ssm = self.session.client('ssm', region_name='us-east-1')


    def test_parameter_value(self):
        # Replace 'my-parameter' with the name of the parameter you want to test
        parameter_name = '/cre/ami-id'
        parameter_value = self.ssm.get_parameter(Name=parameter_name)['Parameter']['Value']
        self.assertEqual(parameter_value, 'ami-06e46074ae430fba6')

if __name__ == '__main__':
    unittest.main()