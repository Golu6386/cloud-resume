import json
import boto3
from botocore.exceptions import ClientError

# Initialize the DynamoDB resource for the ResumeCounter table
# boto3 is the standard AWS SDK for Python, used for interacting with AWS services.
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Resume counter")

def lambda_handler(event, context):
    headers = {
        "Access-Control-Allow-Origin": "*",       
        "Access-Control-Allow-Methods": "GET",
        "Access-Control-Allow-Headers": "Content-Type",
    }

    """
    Main function to increment the visitor count.
    Triggered by API Gateway GET requests.
    
    1. Performs an atomic update on the 'visits' attribute.
    2. Returns the updated count to the frontend.
    """

    # Perform an atomic update: increment the 'visits' count by 1.
    # We use UpdateExpression to ensure the increment happens directly on the DB server,
    # preventing data loss if multiple users visit the site simultaneously.
    try:
        response = table.update_item(
            Key={"id": "visitors"},
            UpdateExpression="SET visitor_count = if_not_exists(visitor_count, :start) + :inc",
            ExpressionAttributeValues={":inc": 1, ":start": 0},
            ReturnValues="UPDATED_NEW",
        )

    # Extract the updated count from the DynamoDB response
        count = int(response["Attributes"]["visitor_count"])
        
    # Return a JSON response formatted for API Gateway (with CORS headers)
        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps({"visitor_count": count}),
        }

    except ClientError as e:
        print(f"DynamoDB error: {e.response['Error']['Message']}")
        return {
            "statusCode": 500,
            "headers": headers,
            "body": json.dumps({"error": "Could not retrieve visitor count"}),
        }
