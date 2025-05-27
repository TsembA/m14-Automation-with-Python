import boto3 
import schedule
from operator import itemgetter
import time

ec2_client = boto3.client('ec2', region_name="us-west-1")

def delete_snapshots():
    volumes = ec2_client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': ['prod', 'dev']
            }
        ]
    )

    for volume in volumes['Volumes']:
        volume_id = volume['VolumeId']
        snapshots = ec2_client.describe_snapshots(
            OwnerIds=['self'],
            Filters=[
                {
                    'Name': 'volume-id',
                    'Values': [volume-id ['volume_id']]
                }
            ]
        )

        sorted_by_date = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)

        for snap in sorted_by_date[2:]:
            response = ec2_client.delete_snapshot(
                SnapshotId=snap['SnapshotId']
            )
            print(response)

schedule.every(30).minutes.do(delete_snapshots)

while True:
    schedule.run_pending()
    time.sleep(1)
