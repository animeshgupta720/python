import boto3
import datetime
import time
import smtplib

from botocore.exceptions import ClientError

ec2 = boto3.resource('ec2')


cloudwatch = boto3.client('cloudwatch', region_name='us-west-1',
    
    # Hard coded strings as credentials, not recommended.
    aws_access_key_id='**',
    aws_secret_access_key='****'
)
print("Now going to start two new instances, skip this step in case you already have instances created.")
#ec2.create_instances(ImageId='ami-063aa838bd7631e0b', MinCount=1, MaxCount=2)
#time.sleep(360)
#for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
   
   #print(status['InstanceId'])
   
a = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

i=0
for instance in a:
	
	#print(instance.id)
	i=i+1
print("The current number of instances is: {}".format(i))

while (1):
	
		d = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
		for instance in d:
			y=instance.id
			#print(y)
			response4 = cloudwatch.put_metric_alarm(
			AlarmName='Web_Server_CPU_Utilization',
			ComparisonOperator='GreaterThanThreshold',
			EvaluationPeriods=1,
			MetricName='CPUUtilization',
			Namespace='AWS/EC2',
			Period=60,
			Statistic='Maximum',
			Threshold=0.50,
			
			ActionsEnabled=True,
			AlarmDescription='Alarm when server CPU exceeds 70%',
			
			Dimensions=[
				{
				  'Name': 'InstanceId',
				  'Value': y
				  
				},
			],
			
			InsufficientDataActions = ['arn:aws:automate:us-west-1:ec2:stop'],
			#print("instance stopped")
			
			)
		print("Waiting for 6 minutes so that the instances are stopped completely before we start new")
		time.sleep(360)
		b=ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
		#print("done")
		c=0
		for instance in b:
			
			
			#print("here2")
			print(instance.id)
			c = c+1

		#print(c)
		if i > c:
			ec2.create_instances(ImageId='ami-063aa838bd7631e0b', MinCount=1, MaxCount=1)
			
			break


print("This is the alarm:")
print(response4)

#Email code

fromaddr = 'animeshgupta720@gmail.com'
toaddrs  = 'animeshgupta720@gmail.com'
msg = ('An instance was shut down because of high CPU and a new instance is started. Please login into the AWS console to verify.')


server = smtplib.SMTP("smtp.gmail.com:587")

#we could getpass() to take password from user. Not shown in this script.

server.starttls()
username='animeshgupta720@gmail.com'
password='*****!'

server.login(username,password)

server.sendmail(fromaddr, toaddrs, msg)
server.quit()
