import boto3

session = boto3.Session(profile_name="default")
ec2_client = session.client("ec2", region_name="us-east-1")

next_token = None

while True:
    if next_token:
        response = ec2_client.describe_instances(NextToken=next_token)
    else:
        response = ec2_client.describe_instances()

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            instance_type = instance["InstanceType"]
            state = instance["State"]["Name"]
            print(
                f"Id da instancia: {instance_id}, Tipo: {instance_type}, Estado: {state}"
            )
    next_token = response.get("NextToken")

    if not next_token:
        break
