import boto3
import json
import logging


def lambda_handler(event, context):
    # Initialize the DynamoDB client
    dynamodb = boto3.client('dynamodb')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    table_name = 'jitto-OA'

    # Get uuid
    item_uuid = event['queryStringParameters']['uuid']
    logger.info(f"got the uuid: {item_uuid}")
    # Get row with matching uuid
    response_body = {}
    http_resp = {}

    try:
        # Retrieve row with matching uuid
        response = dynamodb.get_item(
            TableName=table_name,
            Key={
                'ID': {
                    'S': item_uuid
                }
            }
        )

        item = response.get('Item')
        logger.info(item)

        # Check if it could find anything with a matching uuid
        if item is not None:
            http_resp['statusCode'] = 200
            response_body['item'] = item
            response_body['result'] = 'Item successfully retrieved'
        else:
            http_resp['statusCode'] = 200
            response_body['result'] = 'No item with matching uuid could be found'
    except Exception as e:
        http_resp['statusCode'] = 500
        response_body['result'] = 'Error: ' + str(e)

    http_resp['headers'] = {}
    http_resp['headers']['Content-Type'] = 'application/json'
    http_resp['body'] = json.dumps(response_body)

    return http_resp
