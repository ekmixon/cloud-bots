'''
## ami_set_to_private
What it does: Sets an AMI to be private instead of public
Usage: AUTO: ami_set_to_private
Sample GSL: AMI should have isPublic=false
Limitations: none  
'''

import boto3

def run_action(boto_session,rule,entity,params):
    ami_id = entity['id']
    user_id = entity['ownerId']

    ec2_client = boto_session.client('ec2')

    result = ec2_client.modify_image_attribute(
        ImageId=ami_id,
        LaunchPermission={
            'Remove': [
                {
                    'Group': 'all',
                    'UserId': user_id
                },
            ]
        }
    )

    responseCode = result['ResponseMetadata']['HTTPStatusCode']
    return (
        "Unexpected error: %s \n" % str(result)
        if responseCode >= 400
        else "AMI successfully set to private: %s \n" % ami_id
    ) 
