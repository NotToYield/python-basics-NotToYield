# Products available in the store by category
# Products available in the store by category
import re
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    """Sort the products list by price based on sort_order ('asc' or 'desc')."""
    if sort_order == "asc":
        return sorted(products_list, key=lambda x: x[1])
    elif sort_order == "desc":
        return sorted(products_list, key=lambda x: x[1], reverse=True)
    return products_list


def display_products(products_list):
    """Display products and their prices from a specific category."""
    for i, (name, price) in enumerate(products_list, 1):
        print(f"{i}. {name} - ${price}")


def display_categories():
    """Display available categories and prompt the user to choose one."""
    print("Please choose a category:")
    for i, category in enumerate(products.keys(), 1):
        print(f"{i}. {category}")

    choice = input("Enter category number: ")
    
    if choice.isdigit() and 1 <= int(choice) <= len(products):
        return int(choice) - 1  # Return the selected index
    return None  # Invalid input


def add_to_cart(cart, product, quantity):
    """Add a product to the cart along with the quantity."""
    cart.append((product[0], product[1], quantity))  # Append as (product name, price, quantity)


def display_cart(cart):
    """Display all items in the cart and compute the total cost."""
    total_cost = 0
    for item, price, qty in cart:
        cost = price * qty
        print(f"{item} - ${price} x {qty} = ${cost}")
        total_cost += cost
    print(f"Total cost: ${total_cost}")
    return total_cost


def generate_receipt(name, email, cart, total_cost, address):
    """Generate a receipt with customer details and items purchased."""
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("Items Purchased:")
    for item, price, qty in cart:
        print(f"{qty} x {item} - ${price} = ${price * qty}")
    print(f"Total: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days.")
    print("Payment will be accepted upon delivery.")


def validate_name(name):
    """Validate if the name contains only alphabetic characters, spaces, hyphens, or apostrophes."""
    return bool(re.match(r"^[a-zA-Z\s'-]+$", name))


def validate_email(email):
    """Stricter email validation: checks for valid email format with a domain and TLD."""
    # Basic pattern: local-part@domain.TLD (e.g., john.doe@example.com)
    return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$", email))


def main():
    cart = []
    print("Welcome to the Shopping Program!")
    
    # Get customer name
    name = input("Please enter your name: ")
    while not validate_name(name):
        print("Invalid name. Please try again.")
        name = input("Please enter your name: ")
    
    # Get customer email
    email = input("Please enter your email: ")
    while not validate_email(email):
        print("Invalid email. Please try again.")
        email = input("Please enter your email: ")

    # Shopping process
    while True:
        # Display categories
        category_index = display_categories()
        if category_index is None:
            print("Invalid selection, please try again.")
            continue

        # Get selected category products
        selected_category = list(products.keys())[category_index]
        product_list = products[selected_category]

        # Sort and display products in the selected category
        sort_order = input("Sort products by price? (asc/desc): ").lower()
        product_list = display_sorted_products(product_list, sort_order)
        display_products(product_list)

        # Product selection
        product_choice = input("Select a product number: ")
        if product_choice.isdigit() and 1 <= int(product_choice) <= len(product_list):
            product_index = int(product_choice) - 1
            selected_product = product_list[product_index]

            # Quantity selection
            quantity = input(f"Enter quantity for {selected_product[0]}: ")
            if quantity.isdigit() and int(quantity) > 0:
                add_to_cart(cart, selected_product, int(quantity))
            else:
                print("Invalid quantity, returning to categories.")
        else:
            print("Invalid product selection, returning to categories.")

        # Check if the user wants to continue shopping or finish
        action = input("Enter '1' to continue shopping, '2' to view cart, '3' to finish shopping: ")
        if action == "2":
            display_cart(cart)
        elif action == "3":
            break

    # Cart and receipt
    total_cost = display_cart(cart)
    address = input("Enter your delivery address: ")
    generate_receipt(name, email, cart, total_cost, address)


if __name__ == "__main__":
    main()
