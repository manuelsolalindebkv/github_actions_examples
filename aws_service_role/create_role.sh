#!/bin/bash

export $(cat ../.env | xargs)
# Create new role app-runner-service-role with trust-policy.json
aws iam create-role --role-name app-runner-service-role --assume-role-policy-document file://trust-policy.json
# Attach AWSAppRunnerServicePolicyForECRAccess IAM policy to app-runner-service-role IAM role
aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/service-role/AWSAppRunnerServicePolicyForECRAccess --role-name app-runner-service-role



