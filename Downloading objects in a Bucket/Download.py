'''
@Author: Matheus Barros
Date: 03/06/2021

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

response = s3.list_objects(Bucket='mybucketpopx', #PASSING THE NAME OF THE BUCKET
							MaxKeys=10, #MAX OF OBJECTS TO GET (OPTIONAL)
							Prefix='Files/' #OBJECTS STARTING WITH (OPTIONAL)
							)
response = response['Contents']
#PRINTING FILENAMES
for file in response:

	filename = file['Key'].replace('Files/','')
	print('Downloading ' + filename)
	#DOWNLOADING OBJECTS PASSED AS PARAMETER
	s3.download_file(Filename='Downloads\\'+filename,
					Bucket='mybucketpopx',
					Key=file['Key'])

#GETTING CSVs
df_list = []
for file in response:

	obj = s3.get_object(Bucket='mybucketpopx',
						Key=file['Key'])

	obj_df = pd.read_csv(obj['Body'])
	
	df_list.append(obj_df)

df = pd.concat(df_list).reset_index(drop=True)
print(df)

