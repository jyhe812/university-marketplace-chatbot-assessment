# University Marketplace Insights & Analysis
## Overview:##
Students aren't regular marketplace users. They're broke, busy, and often doing this for the first time. This document covers what I've learned about their needs and how the chatbot should help.

## 1. Common User Pain Points
- **Ghosting & Reliability:** Students often agree to a deal but fail to show up for the meetup, wasting time. 
- **Fragmented Platforms:** Currently, most trading happens on Telegram groups or Carousell, which lack campus-specific moderation and safety filters.
- **Payment Friction:** High anxiety over PayNow/PayLah scams when dealing with "unverified" students.
- **Search Clutter:** Difficulty filtering by specific dorm (e.g., UTown vs. PGPR) or faculty-specific materials (e.g., Year 2 Robotics lab kits)
- **Shipping duration:** If they are getting items from the Marketplace instead of platforms like Shoppe/Lazada/Taobao, more like they are in urgent need of the items. (For eg. exam is tomorrow and they need a calculator), so they cannot wait for the shipping. 

## 2. Safety and Trust Challenges
- **The "Campus Bubble" Illusion:** Students have high initial trust because everyone is "on campus," making them easier targets for phishing or harassment.
- **Adversarial Behavior:** As discussed in Component 3, tech-savvy students use code-words (e.g., "sprayer" for vapes) to bypass automated moderation.
- **In-Person Meetup Risks:** While campus is generally safe, meeting in secluded dorm corridors poses a risk. The chatbot must mandate "Safe Zones" (Library, Canteens, or Student Union).

## 3. Seasonal Patterns (The Campus Cycle)
- **The "Textbook Rush" (Weeks 0-2):** Massive surge in search for core modules. The bot must handle high concurrency and offer pricing comparisons.
- **The "Great Move-Out" (May/Dec):** Excess supply of bulky items (fridges, monitors). Risk of "illegal dumping" in dorm corridors; the bot should push "Quick Sell" tips.
- **Graduation Season:** High demand for graduation gown rentals and photography gear.

## 4. Integration Needs (Systems Thinking)
To be truly effective, the chatbot should integrate with:
- **University SSO (.edu verification):** Mandatory for trust.
- **Module Registration System:** To automatically suggest textbooks based on a student's enrolled modules.
- **Campus Security API:** For one-click reporting of harassment or theft during a transaction.