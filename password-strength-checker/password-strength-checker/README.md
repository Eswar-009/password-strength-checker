# Password Strength Checker

A Python-based password security validator that evaluates password strength using policy checks, entropy estimation, and dictionary leak detection.

## Features

- Password length validation
- Uppercase character detection
- Lowercase character detection
- Digit detection
- Special character detection
- Entropy estimation in bits
- Common password / dictionary leak detection
- Strength classification
- Actionable security feedback
- Command-line interface

## Strength Classification

| Entropy | Classification |
|--------:|----------------|
| < 40 bits | Weak |
| 40–59 bits | Moderate |
| 60–79 bits | Strong |
| 80+ bits | Exceptional |

A password found in the common-password dictionary is classified as Weak regardless of its estimated entropy.

## Requirements

- Python 3.x
- No external packages required

## How to Run

```bash
python password_validator.py
```

Windows alternative:

```bash
py password_validator.py
```

## Example Test Passwords

Weak:
```text
123456
```

Moderate/weak policy example:
```text
Eswar123
```

Strong demo password:
```text
T9!qL7@vR2#pX8
```

Do not use a real personal password for screenshots or demonstrations.

## Security Note

The entropy value is an estimate based on password length and possible character pool. Real-world strength can be lower when passwords contain predictable patterns, dictionary words, or reused credentials.

This project does not send passwords to external services.

## Project Objective

Develop password security validation algorithms that calculate estimated entropy, check policy compliance, detect common passwords, classify strength, and provide actionable security feedback.
