def display_menu(menu):
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ₹{price:.2f}")

def calculate_total(order, menu):
    total = 0
    for item, quantity in order.items():
        if item in menu:
            total += menu[item] * quantity
        else:
            print(f"Item {item} not found in the menu.")
    return total

def apply_gst(total, gst_rate):
    gst_amount = total * gst_rate
    return total + gst_amount

def apply_discount(total, discount):
    return total - discount

# Define the menu
menu = {
    "Chicken Biryani": 250.00,
    "Paneer Butter Masala": 200.00,
    "Lamb Rogan Josh": 300.00,
    "Butter Chicken": 280.00,
    "Vegetable Korma": 180.00,
    "Chole Bhature": 150.00,
    "Dal Makhani": 160.00,
    "Tandoori Chicken": 220.00,
    "Masala Dosa": 120.00,
    "Fish Curry": 260.00,
    "Aloo Paratha": 90.00,
    "Hyderabadi Dum Biryani": 280.00,
    "Mutton Kebab": 250.00,
    "Palak Paneer": 190.00,
    "Prawn Curry": 300.00,
    "Idli Sambar": 80.00,
    "Gulab Jamun": 60.00,
    "Rasgulla": 50.00,
    "Bhel Puri": 70.00,
    "Samosa": 40.00
}

# Display the menu
display_menu(menu)

# Initialize an empty order dictionary
order = {}

# Loop to take order until "done" is entered
while True:
    item = input("Enter item name (type 'done' to finish): ").strip()
    if item == "done":
        break
    
    if item not in menu:
        print("Item not found in the menu. Please enter a valid item.")
        continue
    
    while True:
        try:
            quantity = int(input(f"Enter quantity for {item}: ").strip())
            if quantity % 2 != 0:
                print("Please enter an even quantity.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    order[item] = quantity

# Calculate the total
total = calculate_total(order, menu)
print(f"Subtotal: ₹{total:.2f}")

# Apply GST (e.g., 18% GST rate)
gst_rate = 0.18
total_with_gst = apply_gst(total, gst_rate)
print(f"Total with GST: ₹{total_with_gst:.2f}")

# Apply discount (e.g., ₹50 discount)
discount_amount = 50.00
final_total = apply_discount(total_with_gst, discount_amount)
print(f"Final total after discount: ₹{final_total:.2f}")


