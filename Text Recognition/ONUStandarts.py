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
s3.upload_file(Filename='PlacaONU.jpg',
				Bucket='mybucketpopx',
				Key='Rekognition/PlacaONU.jpg')

'''
#USING IMAGE FROM BUCKET AND USING REKOGNITION
response = rekog.detect_text(
	Image={'S3Object': {'Bucket': 'mybucketpopx',
						'Name': 'Rekognition/PlacaONU.jpg'}
						}
	)['TextDetections']

placa = []

dict_Placas = {
	'1075':'Gás liquefeito de petróleo (GLP)',
	'1661':'Nitroanilina',
	'1223':'Querosene',
	'1294':'Tolueno' 
	}

for i in response:

	if i['Type'] == 'LINE':
		placa.append(i['DetectedText'])


result = dict_Placas.get(placa[1],'Not Found')
if result != 'Not Found':
	print('Material inflamável: ' + result)