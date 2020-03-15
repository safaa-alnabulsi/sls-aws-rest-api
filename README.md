# AWS Serverless REST API

A a proof of concept REST API using Python. It does CRUD operations on Dynamodb table.

## Pre-requisites:

- Nodejs
- Serverless
- Python3.7

## Development 

To create the serverless for the first time

    sls create -p sls-aws-rest-api -t aws-python
        
To create AWS credentials file in ~/.aws

    sls config credentials --provider aws --key <access-key-id> --secret <secret> --profile <profilename>

To invoke function

    sls invoke -f <function-name>
    
To show logs of a function

    sls logs -f <function-name>
    
To tail logs of a function

    sls logs -f <function-name> --tail

## Deployment

To deploy all serverless functions and resources to AWS

    sls deploy -v --email <Your-email>
    sls deploy -v --stage <Your-Stage-Name> --region <AWS-Region>
    
To deploy only the changed function code to AWS

    sls update -v <function-name>
    
To remove all serverless functions and resources deployed to AWS

    sls remove 
    sls remove --stage<Your-Stage-Name> --region <AWS-Region>

## References:
- [Boto3 Dynamodb Client](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#table)
- [Serverless & API Gateway](https://serverless.com/framework/docs/providers/aws/events/apigateway/)
