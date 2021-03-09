'''
@Author: Matheus Barros
Date: 03/06/2021

'''
import boto3
import os

#CREATING CLIENT CONNECTION
AWS_KEY_ID = os.environ['AWS_KEY_ID']
AWS_SECRET = os.environ['AWS_SECRET']

s3 = boto3.client('s3',
					region_name= 'us-east-1',
					aws_access_key_id= AWS_KEY_ID,
					aws_secret_access_key=AWS_SECRET)

response = s3.list_objects(Bucket='mybucketpopx', #PASSING THE NAME OF THE BUCKET
							MaxKeys=10, #MAX OF OBJECTS TO GET (OPTIONAL)
							Prefix='File' #OBJECTS STARTING WITH (OPTIONAL)
							)
#PRINTING FILENAMES
for file in response['Contents']:
	print('File: ' + file['Key']) 