import json
import base64
import gzip
import boto3

sns = boto3.client('sns')

SNS_TOPIC_ARN = "YOUR_SNS_TOPIC_ARN"

def lambda_handler(event, context):

    compressed_payload = base64.b64decode(event['awslogs']['data'])
    uncompressed_payload = gzip.decompress(compressed_payload)
    logs = json.loads(uncompressed_payload)

    for log_event in logs['logEvents']:
        message = log_event['message']

        if "error" in message.lower():
            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject="DevOps Log Alert",
                Message=f"Error detected in logs:\n{message}"
            )

    return {"status": "completed"}