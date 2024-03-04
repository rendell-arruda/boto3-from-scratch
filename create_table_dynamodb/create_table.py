import boto3

session = boto3.Session(profile_name="default")
dynamodb_client = session.client("dynamodb", region_name="us-east-1")

table_name = "customers"

table_schema = [
    {"AttributeName": "customer_id", "AttributeType": "N"},
    {"AttributeName": "email", "AttributeType": "S"},
]

key_schema = [
    {"AttributeName": "customer_id", "KeyType": "HASH"},
    {"AttributeName": "email", "KeyType": "RANGE"},
]

provisioned_throughput = {"ReadCapacityUnits": 5, "WriteCapacityUnits": 5}

response = dynamodb_client.create_table(
    TableName=table_name,
    KeySchema=key_schema,
    AttributeDefinitions=table_schema,
    ProvisionedThroughput=provisioned_throughput,
)

print(f"A tabela {response['TableDescription']['TableName']} foi criada com sucesso")
print(response)
