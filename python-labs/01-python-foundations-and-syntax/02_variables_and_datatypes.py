#!/usr/bin/env python3
"""
Lab 01: Python Foundations - Variables and Core Data Types
Topic: Variable assignment, PEP 8 naming, primitive types (int, float, str, bool, None),
       and type inspection using type() and isinstance().
"""

import sys

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[+] PYTHON VARIABLES & PRIMITIVE DATA TYPES")
print("=" * 60)

# ==============================================================================
# 1. VARIABLE DECLARATION & DYNAMIC TYPING
# ==============================================================================
# Python is dynamically typed: you don't declare types explicitly (e.g. no 'int x = 5').
# The Python interpreter automatically detects the type at runtime.

# PEP 8 Convention: use snake_case for variable names
server_name = "prod-db-server-01"   # String (str)
cpu_cores = 8                       # Integer (int)
cpu_utilization = 74.65             # Floating-point number (float)
is_running = True                   # Boolean (bool) - Note: capitalized True/False
backup_schedule = None              # NoneType (represents absence of value)

# ==============================================================================
# 2. INSPECTING DATA TYPES WITH type()
# ==============================================================================
print("\n--- 1. Variable Values and Types ---")
print(f"server_name     : {server_name:<20} | Type: {type(server_name).__name__}")
print(f"cpu_cores       : {cpu_cores:<20} | Type: {type(cpu_cores).__name__}")
print(f"cpu_utilization : {cpu_utilization:<20} | Type: {type(cpu_utilization).__name__}")
print(f"is_running      : {str(is_running):<20} | Type: {type(is_running).__name__}")
print(f"backup_schedule : {str(backup_schedule):<20} | Type: {type(backup_schedule).__name__}")

# ==============================================================================
# 3. VERIFYING TYPES SAFELY WITH isinstance()
# ==============================================================================
print("\n--- 2. Type Checking with isinstance() ---")
# isinstance(var, ExpectedType) returns True or False
if isinstance(cpu_cores, int):
    print("[PASS] cpu_cores is indeed an integer.")

if isinstance(cpu_utilization, (int, float)):
    print("[PASS] cpu_utilization is numeric (int or float).")

# ==============================================================================
# 4. DYNAMIC REASSIGNMENT
# ==============================================================================
print("\n--- 3. Dynamic Reassignment Demonstration ---")
status_flag = 200
print(f"Initial: status_flag = {status_flag} ({type(status_flag).__name__})")

# Reassign to a string
status_flag = "OK"
print(f"After reassignment: status_flag = '{status_flag}' ({type(status_flag).__name__})")

# ==============================================================================
# 5. MULTIPLE ASSIGNMENT TRICKS
# ==============================================================================
print("\n--- 4. Multiple Assignment Shortcuts ---")
# Assign same value to multiple variables
min_nodes = max_nodes = target_nodes = 3
print(f"Cluster nodes -> Min: {min_nodes}, Max: {max_nodes}, Target: {target_nodes}")

# Unpack multiple values in one line
host, port, protocol = "127.0.0.1", 5432, "postgresql"
print(f"DB Config -> Host: {host}, Port: {port}, Protocol: {protocol}")

print("\n" + "=" * 60)
print("[OK] Variables & Data Types demonstration completed successfully!")
print("=" * 60)
