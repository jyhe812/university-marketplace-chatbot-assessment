# Chatbot Update & Deployment Process

## Overview
To maintain the safety and reliability of the CampusConnect Assistant, we follow a strict CI/CD (Continuous Integration/Continuous Deployment) pipeline. This process ensure that prompt updates—whether for new features or safety patches—are validated against a "Golden Test" suite before reaching the student body.

## 1. Update Workflow
I categorize updates into two types: **Planned Improvements** and **Reactive Patches**.

### Phase A: Identification & Trigger
Updates are triggered by:
- **Policy Changes:** New university regulations (e.g., banning e-scooters on campus).
- **Adversarial Slang Discovery:** Identifying "code words" students use to bypass filters (e.g., listing a vape as a **"sprayer"**, **"juice stick"**, or **"study aid"** for prohibited medications).
- **Performance Gaps:** Addressing failures identified in the `testing-result.md` (e.g., the `edge_001` kitchen knife policy).

### Phase B: Development & Hardening
1. Create a new Git branch: `fix/slang-detection-vape`.
2. Update `prompt.md` to clarify context (e.g., distinguishing between "cleaning spray" and "vape sprayer").
3. Add the new slang terms to the `test-cases.json` suite to ensure future versions remain "hardened" against these terms.

---

## 2. Automated Testing Pipeline
Before any merge, the `automation-concept.py` script is executed. 

**Deployment Gates:**
- **Critical & High Priority:** Must have 100% pass rate. This includes all Safety and Scam-related tests.
- **Regression Testing:** The update must not break existing "Basic Navigation" or "Transaction" features.

---

## 3. Approval & Deployment
- **Review:** A human-in-the-loop (Moderator or Admin) reviews the "Diff" in the prompt to ensure no "instruction drift" has occurred.
- **Merge:** Branch is merged to `main`.
- **API Sync:** The production environment is updated with the new prompt artifact.

---

## 4. Rollback & Safety Procedures
- **Version Control:** Every version of the prompt is tagged in Git with a unique commit hash.
- **Instant Rollback:** If the bot begins to "hallucinate" or incorrectly block legitimate items (e.g., blocking "perfume spray" due to the "sprayer" ban), we use `git revert` to redeploy the last stable version in under 60 seconds.

---

## Workflow Diagram
```text
[Slang/Policy Trigger] 
      ↓
[Edit prompt.md & test-cases.json] 
      ↓
[Execute automation-concept.py] -------------------→ [FAIL: ❌]
      ↓                                                ↓
[PASS: ✅ (All Criticals)]                        (Back to Edit)
      ↓
[Admin Manual Review]
      ↓
[Merge & Deploy to Production]
      ↓
[Monitor Performance] --→ (If issues: Trigger git rollback)