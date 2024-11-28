
email = input("What's your email? ").strip()

if "g" in email:  # The "@" symbol must be in quotes
    print("valid")
else:
    print("invalid")