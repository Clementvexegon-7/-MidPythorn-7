def calculator():
    """Simple calculator for basic arithmetic operations"""

    print("=== Simple Calculator ===")
    print()

    # Get numbers from user
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numbers!")
        return

    # Perform all operations
    print("\n--- Results ---")
    print(f"Sum: {num1} + {num2} = {num1 + num2}")
    print(f"Difference: {num1} - {num2} = {num1 - num2}")
    print(f"Product: {num1} × {num2} = {num1 * num2}")

    # Check for division by zero
    if num2 != 0:
        print(f"Quotient: {num1} ÷ {num2} = {num1 / num2}")
    else:
        print("Quotient: Cannot divide by zero!")


if __name__ == "__main__":
    calculator()