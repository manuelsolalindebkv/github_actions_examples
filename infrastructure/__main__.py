"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws

# login to amazoon ECR registry and get registry name



# Create ECR private repository

# repository_name = "github-actions-ecr-repository"
repository_name = "nodejs"

ecr_repository = aws.ecr.Repository(repository_name,
    # set as public
    image_tag_mutability="MUTABLE",
    image_scanning_configuration={
        "scanOnPush": False
    },
    tags={
        "Name": repository_name
    },
    # set repo name to be the same as the name of the stack
    name=repository_name
)

# print ROLE_ARN and REPOSITORY_URI
pulumi.export('REPOSITORY_URI', ecr_repository.repository_url)


# create apprunner service

apprunner_service = aws.apprunner.Service("apprunner-service",
    service_name="apprunner-service",
    instance_configuration={
        "cpu": "1 vCPU",
        "memory": "2 GB"
    },
    # authentication_configuration={
    #     "connection_arn": "arn:aws:codestar-connections:us-east-1:123456789012:connection/12345678-1234-1234-1234-123456789012"
    # },
    # auto_scaling_configuration={
    #     "max_concurrency": 100,
    #     "max_size": 10,
    #     "min_size": 1
    # },
    # encryption_configuration={
    #     "kms_key": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012"
    # },
    # health_check_configuration={
    #     "healthy_threshold": 2,
    #     "interval": 5,
    #     "path": "/",
    #     "protocol": "HTTP",
    #     "timeout": 2,
    #     "unhealthy_threshold": 2
    # },
    # image_configuration={
    #     "runtime": "NODEJS",
    #     "port": "3000",
    #     "start_command": "npm start"
    # },
    tags={
        "Name": "apprunner-service"
    },
    source_configuration={
        "image_repository": {
            "image_identifier": "123456789012.dkr.ecr.us-east-1.amazonaws.com/nodejs:latest",
            "image_repository_type": "ECR",
            "image_configuration": {
                "port": "3000",
                "runtime": "NODEJS",
                "start_command": "npm start"
            }
        },
        "authentication_configuration": {
            "connection_arn": "arn:aws:codestar-connections:us-east-1:123456789012:connection/12345678-1234-1234-1234-123456789012"
        }
    }
)







