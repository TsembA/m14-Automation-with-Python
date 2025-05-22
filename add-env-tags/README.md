# 🏷️ AWS EC2 Instance Tagging by Region (Python + Boto3)

## 📌 Description

This project is a simple Python script that automates the tagging of all EC2 instances across multiple AWS regions using the **Boto3** SDK. It assigns a specific `env` tag value (`prod` or `dev`) based on the region.

---

## 🌍 Target Regions

- **us-west-1** (California): Tagged with `env=prod`
- **us-west-2** (Oregon): Tagged with `env=dev`

---

## 🔧 Features

- Fetches all EC2 instances in both regions.
- Applies consistent environment tagging to help manage infrastructure.
- Uses `boto3.client` and `boto3.resource` for interaction with AWS EC2.
- Can be extended for multi-region and multi-tag management.

---

## 📁 Project Structure

```bash
ec2-tagging/
├── tag_ec2_by_region.py    # Main script
└── README.md               # Project documentation
```

---

## 💻 Code Overview

```python
import boto3

# Clients and resources for each region
ec2_client_california = boto3.client('ec2', region_name="us-west-1")
ec2_resource_california = boto3.resource('ec2', region_name="us-west-1")

ec2_client_oregon = boto3.client('ec2', region_name="us-west-2")
ec2_resource_oregon = boto3.resource('ec2', region_name="us-west-2")

# Fetch and tag California instances
instance_ids_california = []
reservations_california = ec2_client_california.describe_instances()['Reservations']
for res in reservations_california:
    for ins in res['Instances']:
        instance_ids_california.append(ins['InstanceId'])

ec2_resource_california.create_tags(
    Resources=instance_ids_california,
    Tags=[{'Key': 'env', 'Value': 'prod'}]
)

# Fetch and tag Oregon instances:
instance_ids_oregon = []
reservations_oregon = ec2_client_oregon.describe_instances()['Reservations']
for res in reservations_oregon:
    for ins in res['Instances']:
        instance_ids_oregon.append(ins['InstanceId'])

ec2_resource_oregon.create_tags(
    Resources=instance_ids_oregon,
    Tags=[{'Key': 'env', 'Value': 'dev'}]
)
```

---

## ✅ Requirements

- Python 3.x
- `boto3` library: `pip install boto3`
- AWS credentials configured via:
  - AWS CLI (`aws configure`)
  - IAM Role (if on EC2)
  - Environment variables

---

## 🚀 Use Cases

- Environment-specific tagging for cost tracking and automation.
- Infrastructure organization for DevOps and CloudOps workflows.
- Quick setup for managing regional EC2 resources.