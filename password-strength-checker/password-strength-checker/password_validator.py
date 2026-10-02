import math
import re
import getpass

COMMON_PASSWORDS = {
    "password", "password123", "123456", "12345678", "123456789",
    "1234567890", "qwerty", "qwerty123", "admin", "admin123",
    "letmein", "welcome", "abc123", "iloveyou", "monkey",
    "dragon", "football", "login", "passw0rd"
}


def calculate_entropy(password):
    pool_size = 0

    if re.search(r"[a-z]", password):
        pool_size += 26
    if re.search(r"[A-Z]", password):
        pool_size += 26
    if re.search(r"\d", password):
        pool_size += 10
    if re.search(r"[^a-zA-Z0-9]", password):
        pool_size += 32

    if pool_size == 0:
        return 0

    return len(password) * math.log2(pool_size)


def check_policy(password):
    return {
        "Minimum Length (12+)": len(password) >= 12,
        "Uppercase": bool(re.search(r"[A-Z]", password)),
        "Lowercase": bool(re.search(r"[a-z]", password)),
        "Digit": bool(re.search(r"\d", password)),
        "Special Character": bool(re.search(r"[^a-zA-Z0-9]", password))
    }


def dictionary_check(password):
    return password.lower() in COMMON_PASSWORDS


def classify_strength(password, entropy, leaked):
    if leaked:
        return "WEAK"
    if len(password) < 8 or entropy < 40:
        return "WEAK"
    if entropy < 60:
        return "MODERATE"
    if entropy < 80:
        return "STRONG"
    return "EXCEPTIONAL"


def generate_feedback(password, policy, leaked, entropy):
    feedback = []

    if len(password) < 12:
        feedback.append("Increase password length to at least 12 characters.")
    if not policy["Uppercase"]:
        feedback.append("Add at least one uppercase letter.")
    if not policy["Lowercase"]:
        feedback.append("Add at least one lowercase letter.")
    if not policy["Digit"]:
        feedback.append("Add at least one digit.")
    if not policy["Special Character"]:
        feedback.append("Add at least one special character.")
    if leaked:
        feedback.append("This password is commonly used. Choose a unique password.")
    if entropy < 60:
        feedback.append("Use a longer and more unpredictable password.")

    if not feedback:
        feedback.append("Good password! Keep it unique and never reuse it.")

    return feedback


def display_result(password):
    policy = check_policy(password)
    entropy = calculate_entropy(password)
    leaked = dictionary_check(password)

    strength = classify_strength(password, entropy, leaked)
    feedback = generate_feedback(password, policy, leaked, entropy)

    print("\n" + "=" * 55)
    print("             PASSWORD SECURITY VALIDATOR")
    print("=" * 55)

    print(f"\nPassword Length        : {len(password)} characters")

    print("\nPolicy Checks:")
    for criterion, passed in policy.items():
        status = "PASS" if passed else "FAIL"
        print(f"  {criterion:<22}: {status}")

    print("\nDictionary Leak Check  :",
          "FOUND" if leaked else "NOT FOUND")

    print(f"Estimated Entropy      : {entropy:.2f} bits")

    policy_pass = all(policy.values()) and not leaked
    print("Policy Compliance      :",
          "PASS" if policy_pass else "FAIL")

    print(f"Strength Classification : {strength}")

    print("\nActionable Feedback:")
    for item in feedback:
        print(f"  - {item}")

    print("\n" + "=" * 55)


def main():
    print("=" * 55)
    print("          PASSWORD STRENGTH CHECKER")
    print("=" * 55)

    password = getpass.getpass("\nEnter password: ")

    if not password:
        print("Password cannot be empty.")
        return

    display_result(password)


if __name__ == "__main__":
    main()
