import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')

# Find VPC by Name tag
vpcs = ec2.vpcs.filter(Filters=[{
    'Name': 'tag:Name',
    'Values': ['my-vpc']
}])

# Assuming there's only one matching VPC
vpc = list(vpcs)[0]

# Delete subnets
print(f"\n Deleting subnets in VPC: {vpc.id}")
for subnet in vpc.subnets.all():
    print(f"Deleting subnet: {subnet.id}")
    subnet.delete()

# Delete the VPC
print(f"Deleting VPC: {vpc.id}")
vpc.delete()

print("Cleanup complete.")
