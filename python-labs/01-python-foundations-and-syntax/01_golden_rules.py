#!/usr/bin/env python3
"""
Lab 01: Python Foundations - Golden Rules
Topic: Indentation, Semicolons, and Comments in Python.
"""

import sys

# Ensure UTF-8 output encoding across Windows/Linux terminals
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# ==============================================================================
# RULE 1: INDENTATION IS EVERYTHING (NO CURLY BRACES `{ }`)
# ==============================================================================
# In languages like C, Java, or PHP, blocks of code are wrapped in { }.
# In Python, indentation (standard: 4 spaces per level) defines code blocks!

name = "Alice"
role = "DevOps Engineer"

print("--- Rule 1: Indentation ---")
if name == "Alice":
    # Everything indented inside this block belongs to the 'if' statement
    print(f"Welcome back, {name}!")
    print(f"Your designated role is: {role}")
    
    if role == "DevOps Engineer":
        # Nested block: 8 spaces (2 levels of indentation)
        print("Access granted to Kubernetes cluster & CI/CD pipelines.")

print("This line is outside the if-block because it is NOT indented.\n")


# ==============================================================================
# RULE 2: NO SEMICOLONS NEEDED (;)
# ==============================================================================
# Python statements naturally end at the end of the line.
# While semicolons are technically allowed to separate multiple statements on a single line,
# PEP 8 (Python style guide) strongly discourages their use.

print("--- Rule 2: Clean Line Endings (No Semicolons) ---")
server_ip = "192.168.1.100"
port = 8080
is_active = True

print(f"Connecting to server: {server_ip}:{port} (Active: {is_active})\n")


# ==============================================================================
# RULE 3: COMMENTS USE `#` (HASHTAG / OCTOTHORPE)
# ==============================================================================

# Single-line comment: Python ignores this entire line
service_name = "nginx"  # Inline comment: explains this specific variable

"""
Multi-line Docstring / Comment:
Triple quotes (''' or \"\"\") can span multiple lines.
When not assigned to a variable, they act as documentation or block comments.
"""

print("--- Rule 3: Comments ---")
print(f"Monitoring service: {service_name}")
print("Comments keep code readable and maintainable for team members!\n")


if __name__ == "__main__":
    print("[OK] Rule 1, 2, and 3 executed successfully!")
