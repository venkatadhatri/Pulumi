"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws

size = 't2.micro'
my_ami = 'ami-085925f297f89fce1'
sg_group = 'sg-0371f43c89390a1ed'
my_subnet = 'subnet-0a57be36cc1eaf5de'
my_keyname = 'linux-ci'

server = aws.ec2.Instance("pulumi_test",
    instance_type=size,
    vpc_security_group_ids=[sg_group], # reference security group from above
    ami=my_ami,
    subnet_id=my_subnet,
    key_name=my_keyname,
    tags={
        "Name": "pulumi_test",
    }
    )

pulumi.export('publicIp', server.public_ip)
pulumi.export('publicHostName', server.public_dns)


