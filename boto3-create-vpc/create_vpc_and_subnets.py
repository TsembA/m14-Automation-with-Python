import boto3

# Pass named param <region_name = "us-east-1"> or any other region 
# to check vpcs or do the work in diffirent region
ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

# Create VPC in default region
new_vpc = ec2_resource.create_vpc(
    CidrBlock="10.0.0.0/16"
)
# Create two Subnets for the VPC 
new_vpc.create_subnet(
    CidrBlock="10.0.0.0/24"
)
new_vpc.create_subnet(
    CidrBlock="10.0.2.0/24"
)
# Tag VPC
new_vpc.create_tags(
    Tags=[
        {
            'Key': 'Name',
            'Value': 'my-vpc'
        }
    ]
)

# Discribe availiable VPCs 
all_avail_vpc = ec2_client.describe_vpcs()
vpcs = all_avail_vpc["Vpcs"]

# Chech CidrBlockAssosiationSet for VPC
for vpc in vpcs:
    print(vpc["VpcId"])
    cider_block_assoc_sets = vpc["CidrBlockAssociationSet"]
    for assoc_set in cider_block_assoc_sets:
        print(assoc_set["CidrBlockState"])