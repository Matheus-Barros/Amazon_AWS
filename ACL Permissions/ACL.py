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

#UPLOADING A FILE WITH ACL PUBLIC-READ
'''
filepath = 'Files\\excelfile.xlsx'
s3.upload_file(Filename=filepath,
				Bucket='mybucketpopx',
				Key='excelfile.xlsx',
				ExtraArgs={'ACL':'public-read'}) #private / public-read
'''
#OR IT'S POSSIBLE TO CHANGE THE PRIVACY WITH THE OBJECT ALREADY INSIDE THE BUCKET

s3.put_object_acl(Bucket='mybucketpopx',
					Key='excelfile.xlsx',
					ACL='public-read' # private / public-read
					)

url = "https://{}.s3.amazonaws.com/{}".format('mybucketpopx','excelfile.xlsx')

df = pd.read_excel(url)

print(df)


	