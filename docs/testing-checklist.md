# Testing Checklist

This checklist was used to validate the main customer support flows across both voice and chat.

## Core conversation flows

- [ ] Greeting plays correctly in Amazon Connect
- [ ] Customer input is captured by Amazon Lex V2
- [ ] Lambda receives the Lex event successfully
- [ ] Bedrock Agent is invoked with the correct session ID
- [ ] Lambda returns a valid Lex V2 response
- [ ] Conversation continues normally when no routing flag is set

## Order status flow

- [ ] Bot asks for order ID if it is missing
- [ ] Valid order ID returns order status
- [ ] Invalid order ID is handled gracefully

## Return flow

- [ ] Bot asks for order ID if missing
- [ ] Bot asks for return reason
- [ ] Return flow continues correctly after reason is given

## Escalation flow

- [ ] Customer can ask for a human agent
- [ ] Bedrock action group triggers escalation
- [ ] Lambda returns `escalate=true`
- [ ] Amazon Connect transfers to the configured queue

## End conversation flow

- [ ] Customer can end the interaction naturally
- [ ] Bedrock action group signals end of conversation
- [ ] Lambda returns `endConversation=true`
- [ ] Amazon Connect disconnects the call or chat cleanly

## Knowledge Base flow

- [ ] Policy questions return a relevant answer
- [ ] Retrieval works for return, refund, and shipping questions

## Voice-specific checks

- [ ] Voice interaction works end to end
- [ ] Voice interruption behavior works as expected
- [ ] Responses are short enough for voice playback

## Logging and debugging

- [ ] Lex event is visible in CloudWatch logs
- [ ] Lambda response is logged correctly
- [ ] Errors are visible and easy to trace
