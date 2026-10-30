
print("==========================================")
print("           SHOPPING CART SYSTEM")
print("==========================================")

# Product Catalogue
products = {
    "Pen": 10,
    "Notebook": 50,
    "Bag": 500
}

# Shopping Cart
cart = {}


# Function to display available products
def view_products():
    print("\n----------- AVAILABLE PRODUCTS -----------")
    for name, price in products.items():
        print(f"{name:<15} Rs. {price}")
    print("------------------------------------------")


# Function to add products to cart
def add_to_cart():
    view_products()

    product = input("\nEnter product name: ").strip().title()

    if product not in products:
        print("Invalid product. Available: Pen, Notebook, Bag")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity < 1:
            print("Quantity must be at least 1.")
            return

        if product in cart:
            cart[product] += quantity
        else:
            cart[product] = quantity

        subtotal = sum(products[item] * qty
                       for item, qty in cart.items())

        print(f"{product} x{quantity} added to cart.")
        print(f"Cart subtotal: Rs. {subtotal}")

    except ValueError:
        print("Invalid quantity. Please enter a number.")


# Function to remove products from cart
def remove_from_cart():
    if not cart:
        print("\nYour cart is empty.")
        return

    view_cart()

    product = input("\nEnter product name to remove: ").strip().title()

    if product in cart:
        del cart[product]
        print(f"{product} removed from cart.")
    else:
        print("Product not found in cart.")


# Function to view cart
def view_cart():
    print("\n--------------- YOUR CART ---------------")

    if not cart:
        print("Your cart is empty.")
        return

    subtotal = 0

    for product, quantity in cart.items():
        price = products[product]
        amount = price * quantity
        subtotal += amount

        print(f"{product} x{quantity} = Rs. {amount}")

    print("------------------------------------------")
    print(f"Cart Subtotal: Rs. {subtotal}")


# Function to calculate and generate final bill
def checkout():
    if not cart:
        print("\nYour cart is empty. Add products first.")
        return

    subtotal = sum(products[item] * qty
                   for item, qty in cart.items())

    # Calculate discount
    if subtotal > 500:
        discount = subtotal * 0.10
    else:
        discount = 0

    # GST is calculated after discount
    taxable_amount = subtotal - discount
    gst = taxable_amount * 0.18

    grand_total = taxable_amount + gst

    print("\n==========================================")
    print("                 FINAL BILL")
    print("==========================================")

    for product, quantity in cart.items():
        price = products[product]
        amount = price * quantity
        print(f"{product:<15} x{quantity:<5} Rs. {amount:.2f}")

    print("------------------------------------------")
    print(f"Subtotal          : Rs. {subtotal:.2f}")
    print(f"Discount (10%)    : Rs. {discount:.2f}")
    print(f"GST (18%)         : Rs. {gst:.2f}")
    print("------------------------------------------")
    print(f"GRAND TOTAL       : Rs. {grand_total:.2f}")
    print("==========================================")
    print("       THANK YOU FOR SHOPPING!")
    print("==========================================")

    cart.clear()


# Main Menu
def main():
    print("------------------------------------------")
    print("Welcome to the Shopping Cart System!")
    print("------------------------------------------")
    while True:

        print("\n============= MAIN MENU =============")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")
        print("=====================================")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            view_products()

        elif choice == "2":
            add_to_cart()

        elif choice == "3":
            remove_from_cart()

        elif choice == "4":
            view_cart()

        elif choice == "5":
            checkout()

        elif choice == "6":
            print("***********************************************")
            print("Thank you for using the Shopping Cart System!")
            print("***********************************************")
            
            break

        else:
            print("Invalid choice. Please select 1 to 6.")


# Run the program
if __name__ == "__main__":
    main()
