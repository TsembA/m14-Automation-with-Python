import boto3
import schedule
import time

ec2_client = boto3.client('ec2', region_name="us-west-1")

def check_instance_status():
    print("###############------check_instance_status------###############")
    statuses = ec2_client.describe_instance_status(IncludeAllInstances=True)
    for status in statuses['InstanceStatuses']:
        instance_id = status['InstanceId']
        instance_state = status['InstanceState']['Name']
        instance_status = status['InstanceStatus']['Status']
        system_status = status['SystemStatus']['Status']
        print(f"Instance {instance_id} state: {instance_state} | Instance status: {instance_status} | System status: {system_status}")

# Schedule the job
schedule.every(5).seconds.do(check_instance_status)
schedule.every().monday.at("12:00").do(check_instance_status)

print("EC2 Health Check Scheduler started.")
while True:
    schedule.run_pending()
    time.sleep(1)
