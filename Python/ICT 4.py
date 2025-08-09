list1= []
print("WELCOME TO ADVANCED INVENTORY MANAGEMENT SYSTEM")
print("Press 1 for adding new products: ")
print("Press 2 for updating products :")
print("Press 3 for managing stock levels: ")
print("Press 4 for generating sales report: ")
def prod_add():
    name = input("Product name: ")
    price = input("Product price: ")
    quantity = input("Quantity: ")
    stock = input("Initial stock: ")
    all_prod = {"Name":name, "price":price, "Quantity":quantity, "Stock":stock}
    list1.append(all_prod)
def upd_prod():
    print(list1)


