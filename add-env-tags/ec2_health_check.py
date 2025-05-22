import boto3

ec2_client = boto3.client('ec2', region_name="us-west-1")

# Describe all EC2 instances and print their state
print("EC2 Instance States:")
reservations = ec2_client.describe_instances()

for reservation in reservations['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        state = instance['State']['Name']
        print(f"Instance {instance_id} is currently {state}")

# Describe instance health status
print("\n EC2 Instance Health Checks:")
statuses = ec2_client.describe_instance_status(IncludeAllInstances=True)

for status in statuses['InstanceStatuses']:
    instance_id = status['InstanceId']
    instance_state = status['InstanceState']['Name']
    instance_status = status['InstanceStatus']['Status']
    system_status = status['SystemStatus']['Status']
    
    print(f"Instance {instance_id} state: {instance_state} | Instance status: {instance_status} | System status: {system_status}")
