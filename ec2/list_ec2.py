import boto3

session = boto3.Session(profile_name="default")
ec2_client = session.client("ec2", region_name="us-east-1")

################## WITH NEXT TOKEN ##################
# next_token = None

# while True:
#     if next_token:
#         response = ec2_client.describe_instances(NextToken=next_token)
#     else:
#         response = ec2_client.describe_instances()

#     for reservation in response["Reservations"]:
#         for instance in reservation["Instances"]:
#             instance_id = instance["InstanceId"]
#             instance_type = instance["InstanceType"]
#             state = instance["State"]["Name"]
#             print(
#                 f"Id da instancia: {instance_id}, Tipo: {instance_type}, Estado: {state}"
#             )
#     next_token = response.get("NextToken")

#     if not next_token:
#         break

################## WITH NEXT TOKEN ##################

################## WITH PAGINATOR ##################

paginator = ec2_client.get_paginator("describe_instances")
instance_iterator = paginator.paginate()

## LOOP COMUM

# for page in instance_iterator:
#     for reservation in page["Reservations"]:
#         for instance in reservation["Instances"]:
#             instance_id = instance["InstanceId"]
#             instance_launch_time = instance["LaunchTime"]
#             print(instance_id)
#             print(instance_launch_time)

################## WITH PAGINATOR ##################


## COM FUNCTION
def get_instance_info(instance):
    instance_id = instance["InstanceId"]
    instance_launch_time = instance["LaunchTime"]
    instance_keyName = instance["KeyName"]
    return instance_id, instance_launch_time, instance_keyName


for page in instance_iterator:
    for rervation in page.get("Reservations", []):
        for instance in rervation.get("Instances", []):
            # desempacotamento para retornar multi infos
            instance_id, instance_launch_time, instance_keyName = get_instance_info(
                instance
            )
            print(f"Instance ID: {instance_id}")
            print(f"Launch Time: {instance_launch_time}")
            print(f"Name: {instance_keyName}")
            print()

## COM FUNCTION

################## WITH PAGINATOR ##################
