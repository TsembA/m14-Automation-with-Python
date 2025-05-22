import boto3

ec2_client_california = boto3.client('ec2', region_name="us-west-1")
ec2_resource_california = boto3.resource('ec2', region_name="us-west-1")

ec2_client_oregon = boto3.client('ec2', region_name="us-west-2")
ec2_resource_oregon = boto3.resource('ec2', region_name="us-west-2")

instance_ids_california = []


reservations_california = ec2_client_california.describe_instances()['Reservations']
for res in reservations_california:
    instances = res ['Instances']
    for ins in instances:
        instance_ids_california.append(ins['InstanceId'])


response = ec2_resource_california.create_tags(
    Resources=instance_ids_california,
    Tags=[
        {
            'Key': 'env',
            'Value': 'prod'
        },
    ]
)

instance_ids_oregon = []

reservations_oregon = ec2_client_oregon.describe_instances()['Reservations']
for res in reservations_oregon:
    instances = res ['Instances']
    for ins in instances:
        instance_ids_oregon.append(ins['InstanceId'])
response = ec2_resource_oregon.create_tags(
    Resources=instance_ids_oregon,
    Tags=[
        {
            'Key': 'env',
            'Value': 'dev'
        },
    ]
)