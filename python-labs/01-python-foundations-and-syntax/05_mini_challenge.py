#!/usr/bin/env python3
"""
Lab 01: Python Foundations - Mini Challenge & Practice Quiz
Topic: Interactive server resource estimator and concept quiz to consolidate Lab 01 learning.
"""

import sys

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def run_quiz():
    print("=" * 65)
    print("[?] PYTHON FOUNDATIONS - SELF ASSESSMENT QUIZ")
    print("=" * 65)
    
    questions = [
        {
            "q": "1. What does Python use to define blocks of code?",
            "options": ["A) Curly braces { }", "B) Indentation (spaces/tabs)", "C) Semicolons ;", "D) 'begin' and 'end' keywords"],
            "answer": "B",
            "explanation": "Python strictly uses indentation (PEP 8 recommends 4 spaces) for code blocks."
        },
        {
            "q": "2. What is the return data type of the built-in input() function?",
            "options": ["A) int", "B) auto-detected", "C) str", "D) object"],
            "answer": "C",
            "explanation": "input() always returns a string (str). You must cast it manually to int or float if needed."
        },
        {
            "q": "3. Which of the following values evaluates to False in a boolean context?",
            "options": ["A) -1", "B) '0'", "C) [0]", "D) 0"],
            "answer": "D",
            "explanation": "The number 0 (and 0.0, '', None, [], {}) is Falsy. Note that string '0' is non-empty and thus Truthy!"
        },
        {
            "q": "4. How do you format a float `x = 3.14159` to 2 decimal places using an f-string?",
            "options": ["A) f'{x:2d}'", "B) f'{x:.2f}'", "C) f'{round(2, x)}'", "D) f'{x%2f}'"],
            "answer": "B",
            "explanation": "The format specifier `:.2f` rounds and formats floats to 2 decimal places."
        }
    ]
    
    score = 0
    for item in questions:
        print(f"\n{item['q']}")
        for opt in item['options']:
            print(f"   {opt}")
        print(f"[ANSWER] Correct Answer: {item['answer']}")
        print(f"[REASON] {item['explanation']}")
        score += 1
        
    print("\n" + "-" * 65)
    print(f"[DONE] Review complete! Total concepts covered: {score}/{len(questions)}")
    print("-" * 65)


def resource_calculator():
    print("\n" + "=" * 65)
    print("[+] MINI-TOOL: SERVER CLUSTER CAPACITY CALCULATOR")
    print("=" * 65)
    
    cluster_name = "mlops-gpu-cluster-01"
    total_nodes = 5
    vcpus_per_node = 16
    ram_gb_per_node = 64.0
    storage_tb_per_node = 1.5
    
    total_vcpus = total_nodes * vcpus_per_node
    total_ram = total_nodes * ram_gb_per_node
    total_storage = total_nodes * storage_tb_per_node
    
    print(f"\nCluster Name          : {cluster_name}")
    print(f"Total Worker Nodes    : {total_nodes}")
    print(f"Combined Compute      : {total_vcpus} vCPUs")
    print(f"Combined Memory       : {total_ram:.1f} GB RAM")
    print(f"Combined Raw Storage  : {total_storage:.2f} TB Storage")
    print("=" * 65 + "\n")


if __name__ == "__main__":
    run_quiz()
    resource_calculator()
