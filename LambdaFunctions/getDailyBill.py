
#Module Imports
import datetime
import os
import json
from datetime import timedelta
import boto3
import pandas
from pandas import json_normalize

#Calling the S3 Client
s3_resource = boto3.client('s3')

#Funciton to fetch daily bill
def lambda_handler(event, context):
	today = datetime.date.today()
	key = 'daily-cost-formatted'+ '.csv'
	start = today.re place(day=1).strftime('%Y-%m-%d')
	end = today.strftime('%Y-%m-%d')
	ce = boto3.client('ce')
	bucket = os.environ['BUCKET']
	response = ce.get_cost_and_usage(
	TimePeriod={
	'Start': start,
	'End' : end,
		},
	Granularity ='MONTHLY',
	Metrics=[
	'NetUnblendedCost'
	],
	GroupBy=[
	{
	'Type': 'DIMENSION',
	'Key': 'SERVICE'
	}
	]
	)

	#Converting the response into json format
	data = json.dumps(response['ResultsByTime'][0]['Groups'])

	#Converting the response into Dataframe and renaming the Columns
	df = json_normalize(response['ResultsByTime'][0]['Groups'])
	renamed_df = df.rename(columns = {'Keys':'Services','Metrics.NetUnblendedCost.Amount' : 'Amount','Metrics.NetUnblendedCost.Unit' : 'Currency'}, inplace = True

	#Converting the Dataframe into CSV
	csv_file = df.to_csv()

	#Uploading the file to S3
	s3_resource.put_object(Body=csv_file, Key=key, Bucket=bucket)
	return 0
