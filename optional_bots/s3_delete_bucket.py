'''
## s3_delete_bucket
What it does: Deletes an S3 bucket  
Usage: AUTO: s3_delete_bucket  
Limitations: none  
'''

import boto3

### DeleteS3Bucket ###
def run_action(boto_session,rule,entity,params):
    bucket = entity['id']

    s3_client = boto_session.client('s3')
    result = s3_client.delete_bucket(Bucket=bucket)

    responseCode = result['ResponseMetadata']['HTTPStatusCode']
    return (
        "Unexpected error: %s \n" % str(result)
        if responseCode >= 400
        else "Bucket deleted. Id: %s \n" % (bucket)
    )