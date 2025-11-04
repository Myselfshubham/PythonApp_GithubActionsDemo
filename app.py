#!/usr/bin/env python3
"""
Simple Python application for GitHub Actions demo.
A basic calculator with add, subtract, multiply, and divide functions.
"""

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract second number from first and return the result."""
    return a - b

def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

def divide(a, b):
    """Divide first number by second and return the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def get_operation_result(operation, a, b):
    """Get the result of an operation between two numbers."""
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    
    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")
    
    return operations[operation](a, b)

def main():
    """Main function to demonstrate the calculator."""
    print("Simple Calculator Demo")
    print("=" * 25)
    
    # Example calculations
    examples = [
        ('add', 10, 5),
        ('subtract', 10, 3),
        ('multiply', 4, 7),
        ('divide', 15, 3)
    ]
    
    for operation, a, b in examples:
        try:
            result = get_operation_result(operation, a, b)
            print(f"{a} {operation} {b} = {result}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
