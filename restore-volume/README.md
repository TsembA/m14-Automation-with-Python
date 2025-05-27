
# 🛠️ EC2 Volume Restore and Attach Script (AWS Boto3)

This script automates the process of finding the most recent EBS snapshot for an EC2-attached volume, restoring a new volume from that snapshot, and attaching it to a specified EC2 instance.

## 🚀 Features

- Automatically finds the volume attached to a given EC2 instance.
- Retrieves all snapshots for the volume and selects the most recent one.
- Creates a new EBS volume from the latest snapshot.
- Waits until the new volume becomes available.
- Attaches the new volume to the specified EC2 instance.

## 📋 Requirements

- AWS credentials configured (`~/.aws/credentials` or environment variables)
- IAM permissions for:
  - `ec2:DescribeVolumes`
  - `ec2:DescribeSnapshots`
  - `ec2:CreateVolume`
  - `ec2:AttachVolume`
- Python packages:
  ```bash
  pip install boto3
  ```

## 📌 Usage

1. Set your target EC2 instance ID and region in the script:
   ```python
   instance_id = "i-xxxxxxxxxxxxxxxxx"
   region_name = "us-west-1"
   ```

2. Run the script:
   ```bash
   python ec2_restore_attach.py
   ```

3. The script will:
   - Locate the current volume on the instance
   - Identify the latest snapshot
   - Create a new volume from that snapshot
   - Attach the new volume to the instance as `/dev/xvdb`

## 📎 Notes

- Make sure the new volume’s availability zone matches the instance’s zone (e.g., `us-west-1b`).
- This does **not detach** the existing volume or manage volume limits.
- Device name (`/dev/xvdb`) should not conflict with already attached devices!

## ✅ Example Output

```bash
2024-05-27T12:12:42.000Z
creating new volume from snapshot...
available
Volume attached.
```
