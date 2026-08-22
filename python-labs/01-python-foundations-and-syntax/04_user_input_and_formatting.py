#!/usr/bin/env python3
"""
Lab 01: Python Foundations - User Input & String Formatting
Topic: Capturing CLI user input with input(), type casting user input,
       and modern Python string formatting (F-Strings, padding, precision).
"""

import sys

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[+] USER INPUT & MODERN STRING FORMATTING (F-STRINGS)")
print("=" * 60)

# ==============================================================================
# 1. MODERN F-STRINGS (FORMATTED STRING LITERALS)
# ==============================================================================
# F-strings (introduced in Python 3.6+) are fast, readable, and powerful.

service = "Kubernetes Pod"
cpu_usage = 45.6789
memory_mb = 2048
is_healthy = True

print("\n--- 1. Basic F-String Interpolation ---")
print(f"Service: {service} | Healthy: {is_healthy}")

print("\n--- 2. Number Formatting & Precision in F-Strings ---")
# Round float to 2 decimal places: {:.2f}
print(f"CPU Usage (2 decimals)      : {cpu_usage:.2f}%")

# Comma thousands separator: {:,}
bandwidth_bytes = 104857600
print(f"Bandwidth in bytes          : {bandwidth_bytes:,} bytes")

# Hexadecimal and Binary representations
port_num = 8080
print(f"Port {port_num} in Hex      : {port_num:#x}")
print(f"Port {port_num} in Binary   : {port_num:#b}")

# Alignment and Padding
print("\n--- 3. Column Alignment and Padding ---")
print(f"{'METRIC':<20} | {'VALUE':<10} | {'STATUS':<10}")
print("-" * 46)
print(f"{'CPU Utilization':<20} | {f'{cpu_usage:.1f}%':<10} | {'NORMAL':<10}")
print(f"{'RAM Allocated':<20} | {f'{memory_mb} MB':<10} | {'NORMAL':<10}")
print(f"{'Network Dropped':<20} | {'0 pkts':<10} | {'OPTIMAL':<10}")


# ==============================================================================
# 2. CAPTURING USER INPUT WITH input()
# ==============================================================================
# NOTE: input() always returns data as a STRING ('str').
# To do math, you must cast it to int or float!

print("\n--- 4. Simulated Interactive Input Example ---")
# For automated testing / demo script:
sample_node_name = "worker-node-03"
sample_replicas = "4"
sample_cost_per_hour = "0.75"

print(f"Simulating User Inputs:")
print(f"  Enter node name        : {sample_node_name}")
print(f"  Enter replica count    : {sample_replicas}")
print(f"  Enter hourly rate ($)  : {sample_cost_per_hour}")

# Cast to appropriate types
node_name = sample_node_name
replicas = int(sample_replicas)
cost_per_hour = float(sample_cost_per_hour)

daily_cost = replicas * cost_per_hour * 24
monthly_cost = daily_cost * 30

print("\n--- Summary Report ---")
print(f"Node Identifier    : {node_name}")
print(f"Replicas Scheduled : {replicas}")
print(f"Daily Est. Cost    : ${daily_cost:.2f}")
print(f"Monthly Est. Cost  : ${monthly_cost:,.2f}")

print("\n" + "=" * 60)
print("[OK] User Input & Formatting demonstration completed!")
print("=" * 60)
