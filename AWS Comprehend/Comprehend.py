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

#CONNECTING AWS COMPREHEND
comprehend = boto3.client('comprehend',
					region_name='us-east-1',
					aws_access_key_id=AWS_KEY_ID,
					aws_secret_access_key=AWS_SECRET)

#DISCOVERING LANGUAGE
language = comprehend.detect_dominant_language(Text="Eu odeio aranhas.")['Languages']

print('Language ===>' + str(language) + '\n')


#DISCOVERING SENTIMENT OF PHRASES
response1 = comprehend.detect_sentiment(Text="I hate spiders",
										LanguageCode='en')['Sentiment']

print('Sentiment 1 ===> ' + response1 + '\n')

response2 = comprehend.detect_sentiment(Text="Eu love dogs.",
										LanguageCode='en')['Sentiment']

print('Sentiment 2 ===> ' + response2 + '\n')
