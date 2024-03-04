import boto3

session = boto3.Session(profile_name="default")
s3_client = session.client("s3", region_name="us-east-1")

bucket_name = "rendell-bucket-teste2"
response = s3_client.create_bucket(Bucket=bucket_name)

bucket_response = response["ResponseMetadata"]["HTTPStatusCode"]
print(bucket_response)
