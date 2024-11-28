# Ask the user to enter a year
yr = int(input("Enter a year: "))

# Check and print if it's a leap year
if yr % 400 == 0:
    print("It is a leap year.")
elif yr % 100 == 0:
    print("It is not a leap year.")
elif yr % 4 == 0:
    print("It is a leap year.")
else:
    print("It is not a leap year.")