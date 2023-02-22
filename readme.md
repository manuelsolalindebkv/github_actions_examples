
This repository: https://github.com/manuelsolalindebkv/github_actions_examples.git

# Github actions documentation

https://docs.github.com/en/actions

## Basics

[Understanding GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions)


## Interesting documentation

[How to deploy an AWS Amplify app from Github Actions](https://stackoverflow.com/questions/63354484/how-to-deploy-an-aws-amplify-app-from-github-actions)
[Python App Deploy to AWS App Runner using GitHub Actions](https://dev.to/aws-builders/python-application-deploy-to-aws-app-runner-using-github-actions-f45)


# Python App Deploy to AWS App Runner (image based)

Deploy applications in AWS App Runner with GitHub Actions
Guide: https://aws.amazon.com/es/blogs/containers/deploy-applications-in-aws-app-runner-with-github-actions/

## Initial setup


### 0. Create initial .env file

Create a `.env` file with the following content:

```
AWS_ACCESS_KEY_ID=<your_aws_access_key_id>
AWS_SECRET_ACCESS_KEY=<your_aws_secret_access_key>
AWS_REGION=us-east-1
```

Now go to `aws_service_role` folder and create the service role:

Note: edit role name as required.
```bash
./create_role.sh 
```

Copy the resulting role ARN and add it to the `.env` file:


### 1. Create ECR Private image repository with pulumi

```bash
cd infrastructure
export $(cat ../.env | xargs)
pulumi new aws-python
```

### 2. Add secrets to the github repository


Add github secrets using gh cli, from a `.env` file, for a given repository:

```bash
export REPO=manuelsolalindebkv/github_actions_examples
gh secret set AWS_ACCESS_KEY_ID -b $(cat .env | grep AWS_ACCESS_KEY_ID | cut -d '=' -f2) -R $REPO
gh secret set AWS_SECRET_ACCESS_KEY -b $(cat .env | grep AWS_SECRET_ACCESS_KEY | cut -d '=' -f2) -R $REPO
gh secret set AWS_REGION -b $(cat .env | grep AWS_REGION | cut -d '=' -f2) -R $REPO
gh secret set ROLE_ARN -b $(cat .env | grep ROLE_ARN | cut -d '=' -f2) -R $REPO
```





















