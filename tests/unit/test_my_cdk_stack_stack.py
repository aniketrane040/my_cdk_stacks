import aws_cdk as core
import unittest
import aws_cdk.assertions as assertions
import boto3

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
        self.assertEqual(parameter_value, 'ami-06e46074ae430fba')

if __name__ == '__main__':
    unittest.main()