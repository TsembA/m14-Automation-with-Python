# 🛡️ EC2 Health Monitoring with Python and Boto3

## 📌 Description

A Python-based monitoring tool that checks the health status of Amazon EC2 instances using **Boto3** and **schedule** libraries. It performs frequent and scheduled health checks for visibility into instance states and potential issues.

---

## 🔧 Features

- ✅ Real-time health checks for all EC2 instances
- 🔁 Automatic polling every **5 seconds**
- 🕛 Scheduled check every **Monday at 12:00 PM**
- 📊 Logs instance ID, state, and health statuses

---

## 🧠 How It Works

1. Initializes a Boto3 EC2 client for a specific region (`us-west-1`)
2. Defines a function `check_instance_status()`:
   - Calls `describe_instance_status(IncludeAllInstances=True)`
   - Extracts `InstanceId`, `InstanceState`, `InstanceStatus`, and `SystemStatus`
   - Prints formatted status output
3. Uses the `schedule` library to:
   - Run the function every 5 seconds
   - Run the function every Monday at 12:00 PM
4. Enters a loop with `schedule.run_pending()` for continuous execution

---

## 💻 Code Example

```python
import boto3
import schedule 

ec2_client = boto3.client('ec2', region_name="us-west-1")

def check_instance_status():
    statuses = ec2_client.describe_instance_status(IncludeAllInstances=True)
    for status in statuses['InstanceStatuses']:
        instance_id = status['InstanceId']
        instance_state = status['InstanceState']['Name']
        instance_status = status['InstanceStatus']['Status']
        system_status = status['SystemStatus']['Status']
        print("###############------check_instance_status------###############\n")    
        print(f"Instance {instance_id} state: {instance_state} | Instance status: {instance_status} | System status: {system_status}")

# There's many diffirent option to schedule task, like every 5 seconds
schedule.every(5).seconds.do(check_instance_status)
# Or every monday in certain period of the time 
schedule.every().monday.at("12:00").do(check_instance_status)

while True:
    schedule.run_pending()
