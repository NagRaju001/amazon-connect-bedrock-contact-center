import boto3
import json
import os
import re

bedrock_agent = boto3.client(
    "bedrock-agent-runtime",
    region_name="us-east-1"
)

AGENT_ID = os.environ.get("BEDROCK_AGENT_ID", "REPLACE_ME")
AGENT_ALIAS = os.environ.get("BEDROCK_AGENT_ALIAS_ID", "REPLACE_ME")


def clean(text):
    return re.sub(r"\s+", " ", text).strip()


def lambda_handler(event, context):
    print("EVENT:", json.dumps(event))

    user_input = event.get("inputTranscript", "")
    session_id = event.get("sessionId", "default")

    try:
        agent_response = bedrock_agent.invoke_agent(
            agentId=AGENT_ID,
            agentAliasId=AGENT_ALIAS,
            sessionId=session_id,
            inputText=user_input
        )

        output = ""
        escalate = False
        end_conversation = False

        for chunk_event in agent_response.get("completion", []):
            print("BEDROCK CHUNK EVENT:", str(chunk_event))

            if "chunk" in chunk_event:
                output += chunk_event["chunk"]["bytes"].decode("utf-8")

            if "returnControl" in chunk_event:
                invocation_inputs = chunk_event["returnControl"].get("invocationInputs", [])
                for item in invocation_inputs:
                    func = item.get("functionInvocationInput", {})
                    function_name = func.get("function")

                    if function_name == "escalateToAgent":
                        escalate = True

                    if function_name == "endConversation":
                        end_conversation = True

        output = clean(output)

        if end_conversation:
            response = {
                "sessionState": {
                    "intent": {
                        "name": "FallbackIntent",
                        "state": "Fulfilled"
                    },
                    "dialogAction": {
                        "type": "Close"
                    },
                    "sessionAttributes": {
                        "endConversation": "true",
                        "escalate": "false"
                    }
                },
                "messages": [
                    {
                        "contentType": "PlainText",
                        "content": output if output else "Thank you for contacting us. Goodbye!"
                    }
                ]
            }
            print("LEX RESPONSE:", json.dumps(response))
            return response

        if escalate:
            response = {
                "sessionState": {
                    "intent": {
                        "name": "FallbackIntent",
                        "state": "Fulfilled"
                    },
                    "dialogAction": {
                        "type": "Close"
                    },
                    "sessionAttributes": {
                        "endConversation": "false",
                        "escalate": "true"
                    }
                },
                "messages": [
                    {
                        "contentType": "PlainText",
                        "content": output if output else "Connecting you to an agent."
                    }
                ]
            }
            print("LEX RESPONSE:", json.dumps(response))
            return response

        if not output:
            output = "Sorry, I couldn't understand that."

    except Exception as e:
        print("ERROR:", str(e))
        output = "Something went wrong."

    response = {
        "sessionState": {
            "intent": {
                "name": "FallbackIntent",
                "state": "Fulfilled"
            },
            "dialogAction": {
                "type": "ElicitIntent"
            },
            "sessionAttributes": {
                "endConversation": "false",
                "escalate": "false"
            }
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": output
            }
        ]
    }
    print("LEX RESPONSE:", json.dumps(response))
    return response