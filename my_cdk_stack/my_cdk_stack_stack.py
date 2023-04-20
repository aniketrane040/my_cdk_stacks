from aws_cdk import (
    # Duration,
    Stack,
    aws_ssm as ssm,
    aws_ec2 as ec2
    # aws_sqs as sqs,
)
from constructs import Construct

class MyCdkStackNew(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        parameter_name = '/cre/ami-id'

        # Create an IMachineImage from the SSM parameter
        ssm_image = ec2.MachineImage.from_ssm_parameter(
            parameter_name,
            user_data=ec2.UserData.for_linux(),
            os=ec2.OperatingSystemType.LINUX,
        )

        my_vpc = ec2.Vpc.from_lookup(self, "myvpc", vpc_id='vpc-0514d9d757a7a5dac')

        instance = ec2.Instance(self, 'Instance',
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),
            machine_image=ssm_image,
            vpc= my_vpc,
            key_name='arane-key'
        )






