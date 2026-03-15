import json
import sys

# 1. ADVERSARIAL SLANG MAP
# This allows the system to identify code-words used to bypass safety filters.
SLANG_MAP = {
    "sprayer": "vape",
    "juice stick": "vape",
    "study juice": "unauthorized medication",
    "exam aid": "academic dishonesty service"
}

# 2. LOAD: Read the Golden Test Suite
def load_tests():
    try:
        with open('test-cases.json', 'r') as f:
            return json.load(f)['test_cases']
    except FileNotFoundError:
        print("Error: test-cases.json not found.")
        sys.exit(1)

# 3. TEST: handles new policies and by-pass cases
def get_bot_response(user_input):
    """
    Simulates the Chatbot API. 
    It checks for slang bypasses before providing a standard response.
    """
    input_lower = user_input.lower()
    
    # Check for slang/adversarial naming
    for slang, real_term in SLANG_MAP.items():
        if slang in input_lower:
            return f"Prohibited item detected ({real_term}). Selling this violates campus policy."
    
    # Default response for legitimate marketplace queries
    return "I can help with that. Please remember to meet in public campus areas for safety."

# 4. VALIDATE: The Gatekeeper logic
def run_pipeline():
    print("Starting Automated Deployment Pipeline...")
    print(f"Active slang patches: {list(SLANG_MAP.keys())}")
    
    test_cases = load_tests()
    failed_critical_ids = []

    for case in test_cases:
        response = get_bot_response(case['input'])
        
        # Check if expected keywords are present in the response
        # e.g. For 'sprayer', we expect 'prohibited' to be in the answer
        success = all(item.lower() in response.lower() for item in case['expected_elements'])
        
        # Deployment Gate: Block if any 'critical' safety/slang test fails
        if not success and case.get('priority') == 'critical':
            failed_critical_ids.append(case['id'])

    # 5. DEPLOY OR ROLLBACK
    if failed_critical_ids:
        print(f"DEPLOYMENT BLOCKED: Critical failures in {failed_critical_ids}")
        print("Action: Triggering automated rollback to last stable version.")
        sys.exit(1) 
    else:
        print("ALL CRITICAL TESTS PASSED: Proceeding to production.")
        return True

if __name__ == "__main__":
    run_pipeline()