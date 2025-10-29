"""
Broken Calculator (intentionally violates EXACTLY three principles):
1) KISS
2) DRY
3) Single Responsibility
"""

def add(a, b):
    # Normal add
    return a + b

def add_again(a, b):
    # DRY violation: duplicates add() for no reason
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # keep it simple (no extra flags or globals)
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def calculate_everything():
    """
    Single Responsibility violation:
    - Handles user input, parsing, choosing operations, performing math, and printing results
      all in one place (too many responsibilities).
    """
    print("Broken Calc — type op (add, add2, sub, mul, div) or 'quit'")

    while True:
        op = input("op> ").strip().lower()
        if op == "quit":
            print("bye")
            break

        a_str = input("first number> ")
        b_str = input("second number> ")

        # very basic parse (kept simple to avoid extra unintended violations)
        try:
            a = float(a_str)
            b = float(b_str)
        except ValueError:
            print("numbers only")
            continue

        # KISS violation:
        # long, repetitive if/elif chain instead of a simple dispatch table
        # (unnecessarily complicated branching for a tiny program)
        if op == "add":
            result = add(a, b)
            print("result:", result)
        elif op == "add2":  # intentionally redundant path to same behavior (helps show DRY violation)
            result = add_again(a, b)
            print("result:", result)
        elif op == "sub":
            result = subtract(a, b)
            print("result:", result)
        elif op == "mul":
            result = multiply(a, b)
            print("result:", result)
        elif op == "div":
            try:
                result = divide(a, b)
                print("result:", result)
            except ZeroDivisionError as e:
                print("error:", e)
        else:
            print("unknown op; use add, add2, sub, mul, div, or quit")

if __name__ == "__main__":
    calculate_everything()
