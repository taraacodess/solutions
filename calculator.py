def calc_exp(x, y, z):
    x = int(x)
    y = int(y)
    z = int(z)
    
    # Ask the user for the expression (don't convert to int)
    calc = input("Enter an expression (e.g., x - y, x + y, x / y, x * y): ")

    # Perform the calculation based on the user's input
    if calc == "x + y":
        print(f"{x + y:.2f}")  # Print result with two decimal places

    elif calc == "x - y":
        print(f"{x - y:.2f}")

    elif calc == "x / y":
        if y != 0:  # Prevent division by zero
            print(f"{x / y:.2f}")
        else:
            print("Error: Division by zero.")

    elif calc == "x * y":
        print(f"{x * y:.2f}")

    else:
        print("Invalid expression. Please try again.")