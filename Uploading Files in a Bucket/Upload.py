'''
@Author: Matheus Barros
Date: 03/06/2021

'''
import boto3
import glob
import os

#CREATING CLIENT CONNECTION
AWS_KEY_ID = os.environ['AWS_KEY_ID']
AWS_SECRET = os.environ['AWS_SECRET']

s3 = boto3.client('s3',
					region_name= 'us-east-1',
					aws_access_key_id= AWS_KEY_ID,
					aws_secret_access_key=AWS_SECRET)

path = 'Files\\*'
# Print png images in folder C:\Users\admin\
for filepath in glob.iglob(path):
	file = filepath.replace('Files\\','')

	print('Uploading ' + file)
	s3.upload_file(Filename=filepath,
					Bucket='mybucketpopx',
					Key=file)
	

	
