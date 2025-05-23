# 💾 Automated EC2 Volume Backup (Python + Boto3 + Schedule)

## 📌 Description

This Python script automates the creation of **snapshots (backups)** for Amazon EC2 volumes that are tagged with specific environment names such as `prod` or `staging`. It uses the **Boto3 SDK** to interact with AWS and the **`schedule`** library to run daily backups without manual intervention.

---

## 🔧 Features

- 🏷️ Filters EBS volumes by tag: `Name=prod` or `Name=staging`
- 📸 Creates snapshots of each matched volume
- 🕒 Scheduled to run **daily** using `schedule`
- 📦 Lightweight and easy to run as a background script or cron job alternative

---

## 🧠 How It Works

1. Uses `boto3` to connect to the EC2 service in the `us-west-1` region.
2. Filters volumes based on the `Name` tag (values: `prod`, `staging`).
3. Creates a snapshot for each matching volume.
4. Runs the function once per day using the `schedule` module.

---

## 💻 Example Output

```
{'SnapshotId': 'snap-0a12b34c56d78efgh', 'State': 'pending', ...}
{'SnapshotId': 'snap-0987zyxw654v321tu', 'State': 'pending', ...}
```

---

## 📁 Python Script

```python
import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="us-west-1")

def create_volumes_backup():
    volumes = ec2_client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': ['prod', 'staging']
            }
        ]
    )
    for volume in volumes['Volumes']:
        new_snapshot = ec2_client.create_snapshot(
            VolumeId=volume['VolumeId']
        )
        print(new_snapshot)

schedule.every().day.do(create_volumes_backup)

while True:
    schedule.run_pending()
```

---

## ✅ Requirements

- Python 3.x
- `boto3` (`pip install boto3`)
- `schedule` (`pip install schedule`)
- AWS credentials properly configured (via AWS CLI or environment)

---

## 🚀 Use Cases

- Daily EBS volume backup automation
- Production/staging environment snapshot rotation
- Simple disaster recovery strategy