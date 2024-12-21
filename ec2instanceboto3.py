import boto3

# Create EC2 resource
ec2_resource = boto3.resource('ec2')

# Create EC2 instances
instances = ec2_resource.create_instances(
    ImageId='ami-09b0a86a2c84101e1',  # AMI ID
    MinCount=1,  # Minimum number of instances to launch
    MaxCount=1,  # Maximum number of instances to launch
    InstanceType='t2.micro',  # Instance type
    KeyName='ec2testboto',  # Name of the EC2 key pair
    BlockDeviceMappings = [
        {
            'DeviceName': '/dev/sda1',
            'Ebs': {
                'VolumeSize': 20,
                'VolumeType': 'gp2',
                'DeleteOnTermination': False
            }
        }

    ],
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'FinalEC2Server',  # Instance name tag
                },
                {
                    'Key': 'Env',
                    'Value': 'Preprod'  # Environment tag
                }
            ]
        }
    ],
    UserData = '''#!/bin/bash
    sudo apt update -y
    # Install Apache
    sudo apt install apache2 -y
    sudo systemctl start apache2
    sudo systemctl enable apache2
    echo "<html><body><h1>Hi Eeshan Aggarwal</h1></body></html>" | sudo tee /var/www/html/index.html
    sudo ufw allow 'Apache'
    ''',
)

print("My Instance created")
