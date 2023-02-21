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
pulumi.export('ROLE_ARN', ecr_repository.arn)
pulumi.export('REPOSITORY_URI', ecr_repository.repository_url)




