import boto3
import time
from operator import itemgetter

# Initialize EC2 client and resource in the specified AWS region
ec2_client = boto3.client('ec2', region_name="us-west-1")
ec2_resource = boto3.resource('ec2', region_name="us-west-1")

# Define the EC2 instance ID
instance_id = "i-09e53b1f9a3db5864"

# Retrieve the volume attached to the given EC2 instance
volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'attachment.instance-id',
            'Values': [instance_id]
        }
    ]
)

# Select the first volume from the list
instance_volume = volumes['Volumes'][0]

# Get all snapshots related to this volume
snapshots = ec2_client.describe_snapshots(
    OwnerIds=['self'],
    Filters=[
        {
            'Name': 'volume-id',
            'Values': [instance_volume['VolumeId']]
        }
    ]
)

# Sort snapshots by creation time (newest first) and select the latest one
latest_snapshot = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)[0]
print(latest_snapshot['StartTime'])

# Create a new volume from the latest snapshot
new_volume = ec2_client.create_volume(
    SnapshotId=latest_snapshot['SnapshotId'],
    AvailabilityZone="us-west-1b",
    TagSpecifications=[
        {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'dev'
                }
            ]
        }
    ]
)

# Wait for the new volume to become available, then attach it to the instance
while True:
    vol = ec2_resource.Volume(new_volume['VolumeId']) 
    vol.load()  # Refresh the volume's current state
    print(vol.state)
    if vol.state == 'available':
        ec2_resource.Instance(instance_id).attach_volume(
            VolumeId=new_volume['VolumeId'],
            Device='/dev/xvdb'
        )
        break
    time.sleep(5)  # Add a delay to prevent hammering the API
