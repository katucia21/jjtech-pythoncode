import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    print(event)

    # step -1 # Get transaction ID from URL
    transactionID = event["queryStringParameters"]["transactionID"]

    # step -2 # Get data form dynamoDB for transactionID
    dynamo_db = boto3.resource('dynamodb')

    #step -3 #  return the data fron backend
    table = dynamo_db.Table('jjtech-tran')

    try:
        resp = table.get_item(Key={'partition_key' : transactionID})
        transaction_type = resp["Item"]["transactionType"]
        amount = resp["Item"]["amount"]
        responseJSON = {'transactionID' : str(transactionID), 'transactionType' : transaction_type, 'transactionAmount' : str(amount)}
    except:
        responseJSON = {'Error ': 'Transaction not found'}


    return {
        'statusCode': 200,
        'body': json.dumps(responseJSON)
    }
