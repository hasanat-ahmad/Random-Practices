# Global list to store products
products = []

def add_product():
    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    stock = int(input("Enter Initial Stock: "))
    product = {"product_id": product_id, "name": name, "price": price, "stock": stock}
    products.append(product)
    print(f"{name} added to the inventory.")

def update_stock():
    product_id = input("Enter Product ID to update stock: ")
    new_stock = int(input("Enter New Stock: "))
    for product in products:
        if product["product_id"] == product_id:
            product["stock"] = new_stock
            print(f"Stock updated for {product['name']} (ID: {product['product_id']}). New stock: {new_stock}")
            return
    print(f"Product with ID {product_id} not found.")

def check_inventory():
    print("\nCurrent Inventory:")
    print("ID | Product Name | Price | Stock")
    print("--------------------------------")
    for product in products:
        print(f"{product['product_id']} | {product['name']} | ${product['price']:.2f} | {product['stock']}")

def generate_sales_report():
    total_sales = sum(product['price'] * product['stock'] for product in products)
    print(f"\nTotal Sales: ${total_sales:.2f}")

# Main loop for menu and user interaction
while True:
    print("\nMenu:")
    print("1. Add New Product")
    print("2. Update Stock")
    print("3. Check Inventory")
    print("4. Generate Sales Report")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        update_stock()
    elif choice == "3":
        check_inventory()
    elif choice == "4":
        generate_sales_report()
    elif choice == "5":
        print("Exiting the Inventory Management System.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
