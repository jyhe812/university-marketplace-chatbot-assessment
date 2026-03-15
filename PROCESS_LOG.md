# PROCESS_LOG.md

## 2026-03-15 | 07:42 (SGT)
- **Status:** Project Initialization & Structure Setup
- **Activity:** Created repository using VS Code and pushed to GitHub.
- **Thinking Process:** - Goal: Define a "Campus Assistant" persona that balances helpfulness with strict university policy enforcement.
    - Decided to focus on "Academic Integrity" as a core pillar, as this is a unique requirement for university marketplaces.
    - Chose XML-based prompt structure for better machine readability and control over LLM behavior.

## 2026-03-15 | 09:18 (SGT)
- **Activity:** Completed full execution of 48 test cases and generated the Evaluation Report.
- **Observations:** Identified a policy contradiction in the "Kitchen Knife" edge case where the system prompt was too restrictive compared to the test expectations. 
- **Action:** Drafted prompt revisions to clarify the distinction between culinary tools and weapons.

## 2026-03-15 | 11:29 (SGT)
- **Activity:** Automation & Logic Engineering
- **Observations:** Developed automation-concept.py to implement deterministic safety gates. 
- **Action:** LLMs can be bypassed by evolving student slang (e.g., using "sprayers" to refer to vapes). Therefore I  Engineered a Python-based dictionary mapping layer to "harden" the system.


## 2026-03-15 | 12:32 (SGT)
- **Activity:** Prototyping & Technical Trade-offs
- **Observations:** Lots of online platforms that uses LLM to create apps/chatbots claimed to be free but after several implementations, they asked to pay for premium in order to continue using. Streamlit could not be implemented as I was running out of time. 
- **Action:** Finally get the free app and tested on my prompts after several tries. 

## 2026-03-15 | 01:32 (SGT)
- **Activity:** Final Submission & Documentation Cleanup
