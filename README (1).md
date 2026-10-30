# 🛒 Shopping Cart System

## 📌 Project Overview

The **Shopping Cart System** is a simple console-based application developed using Python. It allows users to browse available products, add items to their shopping cart, remove products, view their cart, and generate a final bill during checkout.

The project demonstrates Python concepts such as dictionaries, functions, loops, conditional statements, exception handling, and basic calculations.

## ✨ Features

- **View Products:** Displays all available products along with their prices.
- **Add to Cart:** Allows users to select products and specify quantities.
- **Remove from Cart:** Removes selected products from the shopping cart.
- **View Cart:** Displays selected products, quantities, and individual amounts.
- **Automatic Subtotal:** Calculates the total cost of all items in the cart.
- **Discount Calculation:** Provides a 10% discount when the subtotal exceeds ₹500.
- **GST Calculation:** Automatically applies 18% GST after deducting the discount.
- **Final Bill Generation:** Displays a detailed bill with subtotal, discount, GST, and grand total.
- **Input Validation:** Handles invalid product names, incorrect quantities, and invalid menu choices.

## 🛍️ Product Catalogue

| Product | Price |
|---|---:|
| Pen | ₹10 |
| Notebook | ₹50 |
| Bag | ₹500 |

## 💰 Billing Logic

The system calculates the final bill using these rules:

1. Calculate the subtotal of all products.
2. Apply a 10% discount if the subtotal is greater than ₹500.
3. Calculate 18% GST on the amount remaining after the discount.
4. Add GST to the discounted amount to get the grand total.

**Formulas:**

- Discount = 10% of subtotal (if subtotal > ₹500)
- Taxable Amount = Subtotal − Discount
- GST = 18% of Taxable Amount
- Grand Total = Taxable Amount + GST

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Concepts Used:**
  - Dictionaries
  - Functions
  - Loops
  - Conditional statements
  - Exception handling (`try-except`)
  - User input and output
  - Dictionary iteration
  - Arithmetic operations

## ▶️ How to Run the Project

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

### Step 2: Download or Clone the Repository

```bash
git clone <your-repository-link>
```

### Step 3: Open the Project Folder

```bash
cd shopping-cart-system
```

### Step 4: Run the Python File

```bash
python shopping_cart.py
```

## 📋 Main Menu

When the program starts, the following menu is displayed:

```text
============= MAIN MENU =============
1. View Products
2. Add to Cart
3. Remove from Cart
4. View Cart
5. Checkout
6. Exit
=====================================
```

Users can enter their choices to perform the desired shopping cart operations.

## 🧾 Sample Bill

For example, if the cart contains 2 pens, 2 notebooks, and 1 bag:

```text
==========================================
                 FINAL BILL
==========================================
Pen             x2    Rs. 20.00
Notebook        x2    Rs. 100.00
Bag             x1    Rs. 500.00
------------------------------------------
Subtotal          : Rs. 620.00
Discount (10%)    : Rs. 62.00
GST (18%)         : Rs. 100.44
------------------------------------------
GRAND TOTAL       : Rs. 658.44
==========================================
       THANK YOU FOR SHOPPING!
==========================================
```

## 🎯 Learning Outcomes

Through this project, I learned how to:

- Create and manage data using Python dictionaries.
- Divide a program into reusable functions.
- Implement a menu-driven application.
- Handle invalid user inputs using exception handling.
- Perform automatic billing and tax calculations.
- Manage shopping cart operations.

## 🚀 Future Improvements

Some features that can be added in future versions:

- Add more products to the catalogue.
- Introduce product search functionality.
- Allow users to update product quantities.
- Add different discount offers and coupons.
- Generate bills in PDF format.
- Store shopping cart details using file handling.
- Create a graphical user interface (GUI).

## 👩‍💻 Author

**Developed as a Python Programming Project.**

---

⭐ If you find this project useful, feel free to explore and improve it!
