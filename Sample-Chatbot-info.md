# Component 5: Chatbot Prototype Information

## Access Information
- Prototype URL: https://partyrock.aws/u/kwskr666/QDUNCWjAS/Compus-Connect-Assistant
- Platform: AWS PartyRock (Generative AI App Builder)

## Rationale for Platform Selection
I selected AWS PartyRock for the following reasons:
1. Accessibility: It provides a hosted, public-facing URL that allows assessors to interact with the bot instantly without local environment setup. Thisi is the only online website I have found to be free after utilising apps such as Coze.com/ loud.dify.ai.
2. Natural Language Understanding: By using Amazon Bedrock, the prototype demonstrates advanced NLU, allowing it to interpret the intent behind adversarial slang rather than relying on simple keyword matching.
3. Rapid Prototyping: It allows for the immediate translation of the System Prompt (developed in Component 1) into a functional UI, proving the prompt's effectiveness in a real-world chat scenario.
4. Professional Engineering Trade-offs: I chose PartyRock because it was the best tool for a 30-minute deadline, but if I had more time, I would definitely use Streamlit. Coding it myself in Streamlit would be better because it allows for actual backend integration and lets you audit the code properly, which is what I’d do for a real engineering project.
## Testing Results
- Scenario: Buying Intent - Successfully provides marketplace navigation and safety tips.
- Scenario: Safety Bypass - When tested with adversarial slang (e.g., "sprayer"), the bot correctly identifies the intent as a prohibited vape sale and blocks the request.
- Scenario: Meetup Advice - Consistently recommends Campus Safe Zones for all transactions.

## Assumptions and Limitations
- Assumptions: Assumes the user is a verified student within the University ecosystem.
- Limitations: The prototype is currently a sandbox version and would require backend database integration to track actual user listings in a production environment.