# University Marketplace Chatbot Assessment

## Introduction
This repository contains my submission for the EPS GenAI Chatbot Systems Engineer assessment. I designed CampusConnect Assistant, an AI support chatbot for a university marketplace where students buy, sell, and trade items within their campus community.

## Approach Overview
I approached this assessment with three principles:
- **Safety First** - Prioritized scam detection, crisis escalation, and prohibited item blocking
- **Context-Aware** - Embedded academic calendar, dorm policies, and campus-specific knowledge
- **Scalable Design** - Built testing framework and update process for long-term maintenance

## How to Review Each Component

| File | What to Look For |
|------|------------------|
| `prompt.md` | XML structure, safety rules, university context |
| `prompt-analysis.md` | Rationale for design decisions |
| `test-cases.json` | Coverage across 5 categories (48 tests) |
| `testing-framework.md` | Evaluation metrics and process |
| `testing-results.md` | Sample pass/fail outcomes |
| `update-process.md` | Version control, testing, deployment, rollback |
| `automation-concept.py` | Pseudo-code for automated testing |
| `marketplace-insights.md` | Student pain points, safety challenges, seasonal patterns |
| `sample-chatbot-info.md` | Live prototype URL and testing instructions |
| `PROCESS_LOG.md` | My thinking process throughout the assessment |

## Key Assumptions

| Assumption | Reasoning |
|------------|-----------|
| .edu email verification | Standard for university platforms |
| On-campus pickup focus | Most students don't have cars |
| Dormitory policies exist | No weapons, alcohol, drugs |
| Academic calendar drives demand | Textbook rushes, move-out sales |
| Students have limited budgets | Price sensitivity is high |
| Scams target students | Young, trusting, have money |

## Time Breakdown

| Component | Time Spent |
|-----------|------------|
| Prompt Design & Engineering | 96 min |
| Test Case Design (48 tests) | 100 min |
| Testing Framework Documentation | 31 min |
| Automation & Update Process | 63 min |
| Marketplace Domain Analysis | 15 min |
| Prototype Development | 32 min |
| Documentation & Final Polish | 30 min |
| **Total** | **6 hours 17 minutes** |

## Next Steps (Real Project)

1. Beta launch with 50 students
2. Measure resolution rate and user satisfaction
3. Integrate .edu verification and course catalog
4. A/B test prompt variations
5. Update based on new scam patterns

## Most Challenging Component

The most challenging part was **thinking of the test cases**. What's written in requirements doesn't always match what users actually want or need. The edge cases are the hardest because you can't predict every weird thing a student might ask. I spent a lot of time just brainstorming scenarios—like students using code words for vapes. These aren't obvious from the prompt alone, but they're real situations that happen. Getting into the mindset of a student (broke, sometimes desperate, sometimes scared) took multiple rounds of thinking and rewriting.

The most challenging part was designing the escalation logic. Deciding when the bot should help versus when it should hand off to a human required balancing safety with efficiency. Getting the thresholds right for threats, self-harm, and scams took multiple iterations.

Also, finding a truly free platform for the prototype was difficult—many claimed to be free but required payment after implementation. Streamlit couldn't be used due to time constraints, but I finally got PartyRock working.

## Three Alternative Approaches Considered

1. The "Keyword & Regex" Blocklist (Deterministic Approach)

Description: This approach uses a hard-coded list of "banned words" and Regular Expressions to instantly kill any message containing prohibited terms.

Why it was rejected: While it is 100% accurate for specific words, it is extremely easy to bypass using basic slang (e.g., writing "v.a.p.e" or "sprayer"). It also lacks "context awareness"—it might block a student selling a "Chef's Knife" for a culinary class because it sees the word "knife," creating a frustrating user experience for legitimate traders.

2. The "LLM-Only" Moderation (Generative Approach)

Description: Relying entirely on the System Prompt and the AI’s internal "moral compass" to decide what is safe and what isn't.

Why it was rejected: LLMs are susceptible to Prompt Injection and "jailbreaking." A clever user could convince a purely LLM-based bot to ignore its safety instructions by using roleplay or complex phrasing. For a government-linked or university safety tool, relying solely on an AI’s "opinion" is too high-risk for a production environment.

3. Human-in-the-Loop Pre-Approval (Manual Approach)

Description: Every listing submitted through the chatbot is held in a "Pending" state until a student moderator or university staff member manually approves it.

Why it was rejected: While this is the safest method, it does not scale. In a university with thousands of students, the delay between posting and listing would kill the marketplace's "real-time" feel. It also creates a massive administrative burden for the university.

I chose a Hybrid Approach:

Deterministic Layer: A Python-based slang dictionary to catch known bypasses instantly (Component 4).

Generative Layer: An LLM to handle the "fuzzy" nuances of conversation and intent detection (Component 5).

This provides the best balance of security (the "Hard Wall") and helpfulness (the "Soft Assistant").

## My Experience with University Marketplaces

From personal experience, when I buy stuff it's usually because I'm in urgent need—exam tomorrow and I don't have the calculator, or I need something last-minute. Speed matters more than price in those moments. When I sell, it's usually bulky stuff I can't bring home—furniture, mini-fridges, things that won't fit in my luggage or my parents' car. I need them gone before the semester ends, or I'm stuck paying for storage. This urgency shaped how I designed the bot: helping buyers find items quickly, and helping sellers understand when to price low for quick sale.