'''
@Author: Matheus Barros
Date: 03/09/2021

'''
import boto3
import os

#CREATING CLIENT CONNECTION
AWS_KEY_ID = os.environ['AWS_KEY_ID']
AWS_SECRET = os.environ['AWS_SECRET']

sns = boto3.client('sns',
					region_name='us-east-1',
					aws_access_key_id=AWS_KEY_ID,
					aws_secret_access_key=AWS_SECRET)

response = sns.create_topic(Name='city_alerts')
topic_arn = response['TopicArn']

'''
					ARN IS A UNIQUE ID OF THE TOPIC
OR WITH A SHORTCUT

topic_arn = sns.create_topic(Name='city_alerts')['TopicArn']
'''

#GETTING TOPICS NAME

response = sns.list_topics()['Topics']

print(response)




