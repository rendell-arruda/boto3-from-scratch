# import boto3

# session = boto3.Session(profile_name="default")
# ec2_client = session.client("ec2", region_name="us-east-1")
# cloudwatch_client = session.client("cloudwatch", region_name="us-east-1")

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

#             # Obtém as métricas de CPU para a instância
#             metrics = cloudwatch_client.get_metric_statistics(
#                 Namespace="AWS/EC2",
#                 MetricName="CPUUtilization",
#                 Dimensions=[{"Name": "InstanceId", "Value": instance_id}],
#                 StartTime="2024-01-01T00:00:00Z",
#                 EndTime="2024-12-31T23:59:59Z",
#                 Period=86400,  # Ajuste o período conforme necessário (por exemplo, para obter métricas diárias)
#                 Statistics=["Average"],
#             )

#             # Verifica se há pontos de dados nas métricas
#             if metrics["Datapoints"]:
#                 average_cpu = metrics["Datapoints"][0]["Average"]
#                 print(
#                     f"Id da instancia: {instance_id}, Tipo: {instance_type}, Estado: {state}, CPU Média: {average_cpu}%"
#                 )
#             else:
#                 print(
#                     f"Id da instancia: {instance_id}, Tipo: {instance_type}, Estado: {state}, Não há dados de CPU disponíveis"
#                 )

#     next_token = response.get("NextToken")

#     if not next_token:
#         break

import boto3
from datetime import datetime, timedelta, timezone

session = boto3.Session(profile_name="default")
ec2_client = session.client("ec2", region_name="us-east-1")
cloudwatch_client = session.client("cloudwatch", region_name="us-east-1")

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

            # Calcula a data e hora atuais
            end_time = datetime.now(timezone.utc)
            # Subtrai 3 dias da data e hora atuais
            start_time = end_time - timedelta(days=3)

            # Obtém as métricas de CPU para a instância nos últimos 3 dias
            metrics = cloudwatch_client.get_metric_statistics(
                Namespace="AWS/EC2",
                MetricName="CPUUtilization",
                Dimensions=[{"Name": "InstanceId", "Value": instance_id}],
                StartTime=start_time,
                EndTime=end_time,
                Period=3600,  # Período de 1 hora, ajuste conforme necessário
                Statistics=["Average"],
            )

            # Verifica se há pontos de dados nas métricas
            if metrics["Datapoints"]:
                average_cpu = metrics["Datapoints"][0]["Average"]
                print(
                    f"Id da instancia: {instance_id}, Tipo: {instance_type}, Estado: {state}, CPU Média nos últimos 3 dias: {average_cpu}%"
                )
            else:
                print(
                    f"Id da instancia: {instance_id}, Tipo: {instance_type}, Estado: {state}, Não há dados de CPU disponíveis nos últimos 3 dias"
                )

    next_token = response.get("NextToken")

    if not next_token:
        break
