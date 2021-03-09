'''
@Author: Matheus Barros
Date: 03/07/2021

'''
import boto3
import os
import pandas as pd

#CREATING CLIENT CONNECTION
AWS_KEY_ID = os.environ['AWS_KEY_ID']
AWS_SECRET = os.environ['AWS_SECRET']

s3 = boto3.client('s3',
					region_name= 'us-east-1',
					aws_access_key_id= AWS_KEY_ID,
					aws_secret_access_key=AWS_SECRET)

#IT'LL GENERATE A TEMPORARY URL, TO ACCESS PRIVATE OBJECTS
share_url = s3.generate_presigned_url(ClientMethod='get_object',
									ExpiresIn=20,#DURATION OF THE URL IN SECONDS
									Params={'Bucket': 'mybucketpopx',
											'Key': 'excelfile.xlsx'
											})
#OPENING FILE WITH PRE-SIGNED URL
df = pd.read_excel(share_url)

print(df)