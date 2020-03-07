# AWS Serverless REST API

## Pre-requisites:

- Nodejs
- Serverless
- Python
- Docker

## Development 

To create the serverless for the first time

    sls create -p sls-aws-rest-api -t aws-python
    
To install python plugin for the first time

    sls plugin install -n serverless-python-requirements
    
To create AWS credentials file in ~/.aws

    sls config credentials --provider aws --key <access-key-id> --secret <secret> --profile <profilename>

To invoke function

    sls invoke -f <function-name>
    
To show logs of a function

    sls logs -f <function-name>
    
To tail logs of a function

    sls logs -f <function-name> --tail

## Deployment
To install python packages in [requirements.txt](requirements.txt)

    npm install --save serverless-python-requirements

To package all the files & installed libraries
   
    sls package
   
To deploy all serverless functions and resources to AWS

    sls deploy -v --email <Your-email>
    sls deploy -v --stage <Your-Stage-Name> --region <AWS-Region> --email <Your-email>
    
To deploy only the changed function code to AWS

    sls update -v <function-name>
    
To remove all serverless functions and resources deployed to AWS

    sls remove 
    sls remove --stage<Your-Stage-Name> --region <AWS-Region>


## References: 
## Pre-requisites:

- Nodejs
- Serverless
- Python
- Docker

## Development 

To create the serverless for the first time

    sls create -p sls-s3-thumbnails -t aws-python
To install python plugin for the first time

    sls plugin install -n serverless-python-requirements
    
To create AWS credentials file in ~/.aws

    sls config credentials --provider aws --key <access-key-id> --secret <secret> --profile <profilename>

To invoke function

    sls invoke -f <function-name>
    
To show logs of a function

    sls logs -f <function-name>
    
To tail logs of a function

    sls logs -f <function-name> --tail

## Deployment
To install python packages in [requirements.txt](requirements.txt)

    npm install --save serverless-python-requirements

To package all the files & installed libraries
   
    sls package
   
To deploy all serverless functions and resources to AWS

    sls deploy -v --email <Your-email>
    sls deploy -v --stage <Your-Stage-Name> --region <AWS-Region> --email <Your-email>
    
To deploy only the changed function code to AWS

    sls update -v <function-name>
    
To remove all serverless functions and resources deployed to AWS

    sls remove 
    sls remove --stage<Your-Stage-Name> --region <AWS-Region>


## References: 