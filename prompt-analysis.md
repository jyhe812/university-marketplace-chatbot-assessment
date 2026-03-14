# Prompt Analysis

### Design Strategy
1. **XML-Style Structuring:** I used `<tag>` delimiters because modern LLMs are optimized to follow instructions more strictly when they are logically separated. This prevents "instruction leakage" where the bot might forget safety rules during long conversations.
2. **Conditional Task Logic:** I implemented an "IF/THEN" structure in the `<task_logic>` section. This ensures the bot provides different, relevant guidance depending on whether the user is a buyer, seller, or reporting a problem.
3. **University-Specific Safety:** Unlike generic marketplaces (e.g., FB Marketplace), a campus environment has high stakes for "Academic Integrity." I prioritized the ban on selling exam/homework materials to align with University code-of-conduct.

### Target Performance
The prompt is designed to minimize "hallucinations" by providing a clear escalation pathway for any scenario that falls outside of basic buying/selling, ensuring that high-risk disputes are handled by humans.