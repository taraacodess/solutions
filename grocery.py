# Create an empty dictionary to store grocery items and their quantities
grocery = {}

print("Enter grocery items (press Ctrl+D to finish):")

try:
    while True:
        # Prompt user for item and convert it to lowercase for case-insensitivity
        item = input().strip().lower()

        # If the item is already in the dictionary, increment its count
        if item in grocery:
            grocery[item] += 1  # Increase the quantity by 1
        else:
            grocery[item] = 1  # If the item is not in the list, add it with quantity 1

except EOFError:
    # This block is triggered when the user presses Ctrl+D

    # Sort the items alphabetically and print the list in uppercase with quantities
    print("\nGrocery List:")
    for item in sorted(grocery):
        print(f"{grocery[item]} {item.upper()}")  # Print each item in uppercase with its count
