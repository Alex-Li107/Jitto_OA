import boto3
import json


def lambda_handler(event, context):
    # Initialize the DynamoDB client
    dynamodb = boto3.client('dynamodb')

    table_name = 'jitto-OA'

    # Get all rows form DB
    response_body = {}
    http_resp = {}

    try:
        # Use the scan operation to retrieve all items from the DynamoDB table
        response = dynamodb.scan(TableName=table_name)

        # Check if the scan operation was successful
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            # Extract the items from the response
            http_resp['statusCode'] = 200
            response_body['items'] = response.get('Items', [])
            response_body['result'] = 'Items successfully retrieved from DynamoDB'
        else:
            http_resp['statusCode'] = response['ResponseMetadata']['HTTPStatusCode']
            response_body['result'] = 'Items unsuccessfully retrieved from DynamoDB'
    except Exception as e:
        http_resp['statusCode'] = 500
        response_body['result'] = 'Error: ' + str(e)

    http_resp['headers'] = {}
    http_resp['headers']['Content-Type'] = 'application/json'
    http_resp['body'] = json.dumps(response_body)

    return http_resp
