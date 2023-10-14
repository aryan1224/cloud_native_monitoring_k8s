import boto3

session = boto3.Session(region_name='ap-south-1')

ecr_client = session.client('ecr')

repository_name = "my-cloud-native-repo"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)
