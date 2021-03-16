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


topics = sns.list_topics()['Topics']

for Arn in topics:
	subscription = sns.list_subscriptions_by_topic(TopicArn=Arn['TopicArn'])['Subscriptions']

	print('Publishing for the following Arn ==> ' + Arn['TopicArn'])

	response = sns.publish(TopicArn = Arn['TopicArn'],
							Message = 'Body text of SMS or e-mail',
							Subject = 'Subject Line for Email'
							)

'''
OR PUBLISH DIRECTLY TO A CELLPHONE
response = sns.publish(
						PhoneNumber = '+199999999',
						Message = 'Body text of SMS or e-mail'
						)
'''