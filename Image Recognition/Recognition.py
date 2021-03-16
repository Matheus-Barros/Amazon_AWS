'''
@Author: Matheus Barros
Date: 03/15/2021

'''
import pandas as pd 
import boto3
import os

#CREATING CLIENT CONNECTION
AWS_KEY_ID = os.environ['AWS_KEY_ID']
AWS_SECRET = os.environ['AWS_SECRET']

s3 = boto3.client('s3',
					region_name='us-east-1',
					aws_access_key_id=AWS_KEY_ID,
					aws_secret_access_key=AWS_SECRET)


rekog = boto3.client('rekognition',
					region_name='us-east-1',
					aws_access_key_id=AWS_KEY_ID,
					aws_secret_access_key=AWS_SECRET)


'''
s3.upload_file(Filename='dog.png',
				Bucket='mybucketpopx',
				Key='Rekognition/dog.png')
'''


response = rekog.detect_labels(
	Image={'S3Object': {'Bucket': 'mybucketpopx',
						'Name': 'Rekognition/dog.png'}},
	MaxLabels=20,
	MinConfidence=95
	)

response = response['Labels']

df = pd.DataFrame(response)

numObjects = []
count = 0

for i in response:
	count = len(i['Instances'])
	numObjects.append(count)

	if count > 0:
		print('Total of {} found: {}'.format(i['Name'],count))
		continue

	print(i['Name'] + ' found')

df = df.assign(Total = numObjects)

df.to_excel('Result.xlsx',index=False)