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

#CREATE A NEW BUCKET
s3.create_bucket(Bucket = 'mybucketpopx')

buckets = s3.list_buckets()

for bucket in buckets['Buckets']:
	print('Bucket: ' + bucket['Name'])

#DELETING A BUCKET
#s3.delete_bucket(Bucket = 'mybucketpopx')

