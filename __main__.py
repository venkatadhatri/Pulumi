"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws
from myconfig import *

def get(name: 'allow-ssh',
        vpc_id: 'vpc-098b4739cdfffa7ca') -> SecurityGroup

server = aws.ec2.Instance("pulumi_test",
    instance_type=size,
    vpc_security_group_ids=[sg_group1,sg_group2], # reference security group from above
    ami=my_ami,
    subnet_id=my_subnet,
    key_name=my_keyname,
    tags={
        "Name": "pulumi-test-1",
    }
    )

pulumi.export('publicIp', server.public_ip)
pulumi.export('publicHostName', server.public_dns)




