'''
@Author: Matheus Barros
Date: 03/16/2021

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

#UPLOAD FILE
'''
s3.upload_file(Filename='Placa-Mercosul.jpg',
				Bucket='mybucketpopx',
				Key='Rekognition/placa-carro.jpg')

'''
#USING IMAGE FROM BUCKET AND USING REKOGNITION
response = rekog.detect_text(
	Image={'S3Object': {'Bucket': 'mybucketpopx',
						'Name': 'Rekognition/placa-carro.jpg'}
						}
	)['TextDetections']


for i in response:

	if i['Type'] == 'LINE':
		print(i['DetectedText'])