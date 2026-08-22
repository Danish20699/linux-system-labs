#!/usr/bin/env python3
"""
Lab 01: Python Foundations - Type Casting & Conversion
Topic: Implicit conversion vs explicit casting (int, float, str, bool),
       truthy/falsy evaluation, and robust error handling during casting.
"""

import sys

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[+] PYTHON TYPE CASTING & CONVERSION")
print("=" * 60)

# ==============================================================================
# 1. IMPLICIT TYPE CONVERSION (AUTOMATIC)
# ==============================================================================
# Python automatically converts smaller types to wider types to prevent data loss.
num_int = 10        # int
num_float = 4.5     # float
result = num_int + num_float  # int + float becomes float

print("\n--- 1. Implicit Type Conversion ---")
print(f"{num_int} ({type(num_int).__name__}) + {num_float} ({type(num_float).__name__}) = {result} ({type(result).__name__})")


# ==============================================================================
# 2. EXPLICIT TYPE CASTING (MANUAL)
# ==============================================================================
print("\n--- 2. Explicit Type Casting ---")

# A. String to Integer / Float
str_port = "8080"
str_latency = "12.34"

int_port = int(str_port)
float_latency = float(str_latency)

print(f"String '{str_port}' -> Integer: {int_port} (Type: {type(int_port).__name__})")
print(f"String '{str_latency}' -> Float: {float_latency} (Type: {type(float_latency).__name__})")

# B. Float to Integer (Truncates the decimal part, does NOT round)
score = 98.85
truncated_score = int(score)
print(f"Float {score} -> int(score): {truncated_score} (Notice: truncated, not rounded)")

# C. Number to String
max_connections = 500
msg = "Server capacity: " + str(max_connections) + " clients"
print(f"Number to String concatenation: {msg}")


# ==============================================================================
# 3. BOOLEAN CASTING (TRUTHY vs FALSY VALUES)
# ==============================================================================
print("\n--- 3. Truthy vs Falsy Values ---")
# In Python, the following evaluate to False (Falsy):
# 0, 0.0, "", None, False, [], (), {}, set()
# Everything else evaluates to True (Truthy).

falsy_values = [0, 0.0, "", None, [], {}]
truthy_values = [1, -5, "DevOps", 3.14, [1, 2], {"env": "prod"}]

print("Falsy evaluations:")
for val in falsy_values:
    print(f"  bool({repr(val):<10}) -> {bool(val)}")

print("\nTruthy evaluations:")
for val in truthy_values:
    print(f"  bool({repr(val):<10}) -> {bool(val)}")


# ==============================================================================
# 4. HANDLING CONVERSION ERRORS (ROBUST SCRIPTING)
# ==============================================================================
print("\n--- 4. Safe Type Casting Pattern ---")

raw_user_inputs = ["100", "42", "hello_world", "3.14", "99"]

for raw in raw_user_inputs:
    try:
        converted = int(raw)
        print(f"  [SUCCESS] Successfully converted '{raw}' to integer {converted}")
    except ValueError:
        print(f"  [ERROR] Cannot convert '{raw}' to integer (ValueError caught)")

print("\n" + "=" * 60)
print("[OK] Type Casting & Conversion demonstration completed!")
print("=" * 60)
