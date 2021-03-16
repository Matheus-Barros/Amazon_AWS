'''
@Author: Matheus Barros
Date: 03/10/2021

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

response = sns.list_topics()['Topics']

#LISTING SUBSCRIPTIONS
for Arn in response:
	list_subscriptions_by_topic = sns.list_subscriptions_by_topic(
								TopicArn= Arn['TopicArn'])['Subscriptions']
	print(list_subscriptions_by_topic)