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

#GETTING TOPIC NAMES
response = sns.list_topics()['Topics']
for topicArn in response:

	#LISTING SUBSCRIPTIONS
	list_subscriptions_by_topic = sns.list_subscriptions_by_topic(
									TopicArn= topicArn['TopicArn'])['Subscriptions']

	#DELETING SUBSCRIPTIONS
	for sub in list_subscriptions_by_topic:
		if sub['Protocol'] == 'sms':
			print('Unsubscribing ==> ' + sub['SubscriptionArn'])
			sns.unsubscribe(SubscriptionArn = sub['SubscriptionArn'])
