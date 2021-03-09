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


response = s3.list_objects(Bucket='mybucketpopx')

objs_df = pd.DataFrame(response['Contents'])

base_url = 'https://mybucketpopx.s3.amazonaws.com/'

print(list(objs_df))

objs_df['Link'] = base_url + objs_df['Key']
objs_df.to_html('report_listing.html',
				columns=['Link','LastModified','Size'],
				render_links=True,
				border=1)

s3.upload_file(Filename='report_listing.html',
				Bucket='mybucketpopx',
				Key='table.html',
				ExtraArgs = {'ContentType': 'text/html',
							'ACL': 'public-read'}
				)

