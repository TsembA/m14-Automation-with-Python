# 🧹 Automated EC2 Snapshot Cleanup (Python + Boto3)

## 📌 Description

This script automatically cleans up old Amazon EBS snapshots for EC2 volumes tagged with `prod` or `dev`. It retains only the **two most recent snapshots per volume** and deletes the rest using the **Boto3 AWS SDK**. The task is scheduled to run every 30 minutes using the `schedule` library, helping to enforce backup retention policies and control storage costs.

---

## 🔧 Features

- ✅ Scans EC2 volumes filtered by tag: `Name=prod` or `Name=dev`
- 📸 Retrieves all snapshots for each matching volume
- 🔁 Keeps only the **2 most recent** snapshots per volume
- ❌ Deletes older snapshots
- ⏱ Scheduled to run **every 30 seconds** using `schedule`

---

## 💻 Python Script

```python
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
                    'Values': [volume_id]
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
```

---

## ✅ Requirements

- Python 3.x
- `boto3` (`pip install boto3`)
- `schedule` (`pip install schedule`)
- AWS credentials configured via:
  - `~/.aws/credentials`
  - Environment variables
  - IAM role (if running on EC2)

---

## 🧪 Use Cases

- Clean up outdated snapshots to reduce EBS storage costs
- Enforce retention policy (e.g., keep only 2 most recent backups)
- Automate EC2 volume snapshot hygiene across environments
