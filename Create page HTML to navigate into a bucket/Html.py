'''
@Author: Matheus Barros
Date: 03/09/2021

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

#LIST THAT WILL KEEP ALL THE DATAFRAMES
df_list = []

#LISTING OBJECTS
response = s3.list_objects(Bucket='mybucketpopx',
							Prefix='File')

request_files = response['Contents']

#GETTING OBJECTS
for file in request_files:

	obj = s3.get_object(Bucket='mybucketpopx',
						Key=file['Key'])

	obj_df = pd.read_csv(obj['Body'])

	#APPENDING TO LIST
	df_list.append(obj_df)


#CONCATING DATAFRAME
df = pd.concat(df_list)

df = df.reset_index(drop=True)

df.to_csv('Name_and_Cities.csv')
df.to_html('Name_and_Cities.html')

#UPLOADING FILES
s3.upload_file(Filename='Name_and_Cities.csv',
				Bucket='mybucketpopx',
				Key='Files/Final-Report/Name_and_Cities.csv',
				ExtraArgs={
					'ACL':'public-read'
				})

s3.upload_file(Filename='Name_and_Cities.html',
				Bucket='mybucketpopx',
				Key='Files/Final-Report/Name_and_Cities.html',
				ExtraArgs={
					'ACL':'public-read',
					'ContentType': 'txt/html'
				})


#===============CREATING AN INDEX OF ALL FILES IN THE BUCKET============
response = s3.list_objects(Bucket='mybucketpopx',
							Prefix='File')

objects_df = pd.DataFrame(response['Contents'])

#CREATING COLUMN WITH THE LINK OF EACH OBJECT
base_url = 'https://mybucketpopx.s3.amazonaws.com/'
objects_df['Link'] = base_url + objects_df['Key']

#CREATING AN INDEX
objects_df.to_html('index.html',
					columns = ['Link','LastModified', 'Size'],
					render_links=True)

#UPLOADING FILES
s3.upload_file(Filename='index.html',
				Key='index.html',
				Bucket='mybucketpopx',
				ExtraArgs = {
					'ContentType': 'text/html',
					'ACL': 'public-read'
				})