# Restaurant Billing System

## Overview

This Python script is a simple restaurant billing system that allows users to place orders from a menu, calculates the total amount including GST, applies any discounts, and displays the final amount. The script is designed for ease of use and flexibility.

## Features

- **Display Menu:** Shows a list of menu items with their prices.
- **Place Order:** Allows users to enter the name and quantity of items they wish to order.
- **Calculate Total:** Computes the subtotal based on the order.
- **Apply GST:** Adds GST to the total amount.
- **Apply Discount:** Subtracts a discount amount from the total.
- **Editable Menu:** The menu is customizable and can be updated to include new items or change existing ones.

## Menu

The menu is defined in the script and can be edited directly in the code. Here is an example of the menu items available:

- Chicken Biryani: ₹250.00
- Paneer Butter Masala: ₹200.00
- Lamb Rogan Josh: ₹300.00
- Butter Chicken: ₹280.00
- Vegetable Korma: ₹180.00
- Chole Bhature: ₹150.00
- Dal Makhani: ₹160.00
- Tandoori Chicken: ₹220.00
- Masala Dosa: ₹120.00
- Fish Curry: ₹260.00
- Aloo Paratha: ₹90.00
- Hyderabadi Dum Biryani: ₹280.00
- Mutton Kebab: ₹250.00
- Palak Paneer: ₹190.00
- Prawn Curry: ₹300.00
- Idli Sambar: ₹80.00
- Gulab Jamun: ₹60.00
- Rasgulla: ₹50.00
- Bhel Puri: ₹70.00
- Samosa: ₹40.00

## Installation

To run the script on your local machine:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/restaurant-billing-system.git
    ```

2. **Navigate to the project directory:**
    ```sh
    cd restaurant-billing-system
    ```

3. **Ensure you have Python installed.**

4. **Run the script:**
    ```sh
    python restaurant_billing_system.py
    ```

## How to Use

1. **Start the Script:** Run `python restaurant_billing_system.py`.
2. **Place Order:** Enter the name and quantity of items you want to order. Type 'done' when you finish ordering.
3. **View Results:** The script will display the subtotal, total with GST, and final amount after applying the discount.

## Example

An example interaction with the script:

Menu:
Chicken Biryani: ₹250.00
Paneer Butter Masala: ₹200.00
...

Enter item name (type 'done' to finish): Chicken Biryani
Enter quantity for Chicken Biryani: 2

Enter item name (type 'done' to finish): Paneer Butter Masala
Enter quantity for Paneer Butter Masala: 4

Enter item name (type 'done' to finish): done

Subtotal: ₹1400.00
Total with GST: ₹1652.00
Final total after discount: ₹1602.00


## Files

- **restaurant_billing_system.py:** The main script containing the billing system logic.

## Editing the Menu

To edit the menu, open the `restaurant_billing_system.py` file and modify the `menu` dictionary. You can add new items, remove existing ones, or update prices as needed.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.


## Acknowledgments

Thanks to the Python documentation and the programming community for resources and support.
