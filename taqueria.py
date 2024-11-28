menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0

print("Enter items (press Ctrl+D to finish):")

try:
    while True:
        item = input("Enter item: ").title()  # Use .title() directly to format input
        if item in menu:  # If the item is found in the menu
            total += menu[item]  # Add the price of the item to the total
            print(f"Total so far: ${total:.2f}")
        else:
            print(f"Sorry, {item} is not on the menu.")

except EOFError:     
    print("\nThank you! Final Total: ${total:.2f}")  # When Ctrl+D is pressed
