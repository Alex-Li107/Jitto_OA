import boto3
import json
import uuid


def lambda_handler(event, context):
    # Initialize the DynamoDB client
    dynamodb = boto3.client('dynamodb')

    table_name = 'jitto-OA'

    # Get item to add from POST request
    name = event['queryStringParameters']['name']
    description = event['queryStringParameters']['description']
    item_uuid = uuid.uuid4()

    # item to insert into db
    item = {
        'ID': {
            'S': str(item_uuid)
        },
        'Name': {
            'S': name
        },
        'Description': {
            'S': description
        }
    }
    response_body = {}
    http_resp = {}

    try:
        # Insert the item into the DynamoDB table
        dynamodb.put_item(TableName=table_name, Item=item)

        response_body['result'] = 'Item successfully added to DynamoDB'
        http_resp['statusCode'] = 200
    except Exception as e:
        response_body['result'] = 'Error: ' + str(e) + '. Item unsuccessfully added'
        http_resp['statusCode'] = 500

    http_resp['headers'] = {}
    http_resp['headers']['Content-Type'] = 'application/json'
    http_resp['body'] = json.dumps(response_body)

    return http_resp
