# Setup Guide

This repository contains a public-safe version of the project structure and selected implementation files.

## Main AWS services used

- Amazon Connect
- Amazon Lex V2
- AWS Lambda
- Amazon Bedrock Agents
- Amazon Bedrock Knowledge Bases
- Amazon Bedrock Guardrails
- DynamoDB
- Amazon S3
- OpenSearch Serverless
- Amazon Polly
- CloudWatch Logs

## High-level setup flow

1. Create the Amazon Connect instance and contact flow
2. Create the Lex V2 bot and connect it to Amazon Connect
3. Deploy the Lambda bridge function
4. Create the Bedrock Agent and configure action groups
5. Configure the Knowledge Base and upload support documents
6. Create sample DynamoDB tables for order and return flows
7. Connect session attributes for escalation and end-conversation routing
8. Test both voice and chat scenarios

## Environment configuration

The Lambda function expects Bedrock Agent configuration through environment variables.

Example:

- `BEDROCK_AGENT_ID`
- `BEDROCK_AGENT_ALIAS_ID`

## Public repo note

This repository does not include:

- private AWS account details
- production ARNs
- raw service exports
- secrets or credentials
- real customer data

Use your own AWS resources and configuration when recreating the project.
