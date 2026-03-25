# Amazon Connect Flow Notes

This project uses Amazon Connect as the entry point for both voice and chat interactions.

## Main flow

The contact flow follows this pattern:

1. Play greeting
2. Get customer input using Amazon Lex V2
3. Check whether `endConversation` is `true`
4. If yes, disconnect the contact
5. If not, check whether `escalate` is `true`
6. If yes, route to a queue and transfer to a human agent
7. If not, continue the conversation loop

## Session attributes used

- `endConversation`
- `escalate`

These values are returned by Lambda through the Lex response and are used by Connect for routing decisions.

## Notes

- The same architecture supports both chat and voice
- Voice interruption behavior was enabled through Lex session settings
- Raw contact flow exports are not included in this public repository
