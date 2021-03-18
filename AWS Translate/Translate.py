'''
@Author: Matheus Barros
Date: 03/18/2021

'''
import pandas as pd 
import boto3
import os

#CREATING CLIENT CONNECTION
AWS_KEY_ID = os.environ['AWS_KEY_ID']
AWS_SECRET = os.environ['AWS_SECRET']

#CONNECTING AWS TRANSLATE
translate = boto3.client('translate',
					region_name='us-east-1',
					aws_access_key_id=AWS_KEY_ID,
					aws_secret_access_key=AWS_SECRET)

#TRANSLATING PHRASE
response = translate.translate_text(Text='Hallo. Ich bin Matheus. Wie heißen Sie?',
									SourceLanguageCode='auto',
									TargetLanguageCode='en')

print(response)







