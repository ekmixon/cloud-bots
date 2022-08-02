'''
## ec2_terminate_instance
What it does: Terminates an ec2 instance  
Usage: AUTO: ec2_terminate_instance  
Limitations: none  
'''

import boto3

def run_action(boto_session,rule,entity,params):
    instance = entity['id']
    ec2_client = boto_session.client('ec2')

    result = ec2_client.terminate_instances(InstanceIds=[instance])

    responseCode = result['ResponseMetadata']['HTTPStatusCode']
    return (
        "Unexpected error: %s \n" % result
        if responseCode >= 400
        else "Instance terminated: %s \n" % instance
    )