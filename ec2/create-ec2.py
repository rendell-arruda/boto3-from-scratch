import boto3

ec2_client = boto3.client("ec2", region_name="us-east-1")

instace_type = "t2.micro"
ami_instance = "ami-0440d3b780d96b29d"

response = ec2_client.run_instances(
    ImageId=ami_instance, InstanceType=instace_type, MaxCount=1, MinCount=1
)
#  Devolve um dict{['Key']:['Value']}com uma lista[0,1,2] de varios dicts{['Key']:['Value'],['Key']:['Value']}
instace_id = response["Instances"][0]["InstanceId"]
print(instace_id)
