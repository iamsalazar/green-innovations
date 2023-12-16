def get_aws_data(file_name):
    import boto3
    import os
    import pandas as pd

    aws_access_key= os.environ.get("ACCESS_KEY")
    aws_secret_key= os.environ.get("SECRET_KEY")
    project_path = os.environ.get("PROJECT_PATH")
    
    session = boto3.Session(
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name='us-east-1'
    )

    s3 = session.client('s3')

    response = s3.get_object(Bucket='greeninnovations', Key=file_name)

    df = pd.read_csv(response['Body'], encoding='utf-8',low_memory=False)
    return df

