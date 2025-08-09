import msvcrt

class Product(object):
    
    def __init__(self,ID, name, price, stock):
        self.name = name
        self.price = price
        self.ID = ID
        self.stock = stock
        
    def addProduct(self,ID , name, price, stock): # Adds products to inventory
        inp = Product(ID,name,price, stock)
        list1.append(inp)
        print("The Product has been added: ")
        print(f"ID\tName\tPrice\tStock")
        for i in range(len(list1)):
            if ID == list1[i].ID:
                print(f"{list1[i].ID}\t{list1[i].name}\t{list1[i].price:.2f}\t{list1[i].stock}")
            
    def showAllProducts(self, ):    # Displays all products in the inventory
        print(f"ID\tName\tPrice\tStock")
        for i in range(len(list1)):
            print(f"{list1[i].ID}\t{list1[i].name}\t{list1[i].price:.2f}\t{list1[i].stock}")

    def searchProduct(self, ID):    # Searches the inventory for the product by ID matching
        notCheck = True
        for i in range(len(list1)):
            if ID == list1[i].ID:
                print("The product has been found!")
                print(f"ID\tName\t\tPrice\tStock")
                print(f"{list1[i].ID}\t{list1[i].name}\t\t{list1[i].price:.2f}\t{list1[i].stock}")
                notCheck = False
                break
        if notCheck:
            print("Product not found!")
            
                
    def delProduct(self,ID):    # Deletes product from inventory and updates the ID of all products.
        for i in range(len(list1)):
            if ID == list1[i].ID:
                delCheck = i
        del list1[delCheck]
        for i in range(len(list1)):
            if list1[i].ID > ID:
                list1[i].ID -= 1
                
    def updateProduct(self, ID, name, price, choice): # Updates the name or price of the product
        for i in range(len(list1)):
            if ID == list1[i].ID:
                if choice == 1:
                    list1[i].name = name
                elif choice == 2:
                    list1[i].price = price
                elif choice == 3:
                    list1[i].name = name
                    list1[i].price = price
    
    def updateStock(self,ID,stock):     # Updates the price of the product
        for i in range (len(list1)):
            if ID == list1[i].ID:
                list1[i].stock = stock
                
    def salesReport(self):
        totalRevenue = 0
        productIDS = []
        stockSold = []
        productsSold = int(input("Enter the different number of products that have been sold: "))
        for i in range (productsSold):
           search = int((input("Enter the ID of the product: ")))
           productIDS.append(search)
           IDSold = int(input("Enter the amount of stock sold: "))
           stockSold.append(IDSold)
           
        print(f"\n\n\tSales Report\t")
        print(f"ID\tName\tPrice\tStock Sold\tTotal Profit")
        for i in productIDS:
            for j in range(len(list1)):
                if productIDS[i] == list1[j].ID:
                    print(f"{list1[j].ID}\t{list1[j].name}\t{list1[j].price}\t{stockSold[i]}\t\t{list1[j].price * stockSold[i]}")
                
        
            
        
list1 = [] 
prod = Product(0,'',0.0,0)
ID = 0
while True:
    print("Welcome to the IMS! ")
    print("Functions Available:\n1.)Add a Product\n2.)List all the products\n3.)Search a Product\n4.)Update a Product\n5.)Delete a Product\n6.)Update Stock\n7.)Generate Sales Report\n8.)Exit the program")
    try:
        operationPerform = int(input("Enter the corresponding number to perform an operation: "))
        if operationPerform == 8:
            break
        if operationPerform < 1 or operationPerform > 8:
            raise ValueError("Invalid Value Entered")
    except:
        print("Invalid Input, Please enter a numeric value between 1-5\n\nPress Enter to continue")
        msvcrt.getch()
        
    if operationPerform == 1:
        name = input("Enter the name of the product: ")
        price = float(input("Enter the price of the product: "))
        stock = int(input("Enter the number of available stock of the product: "))
        prod.addProduct(ID,name,price, stock)
        print("\nPress Enter to continue")
        msvcrt.getch()
        ID += 1
        
    elif operationPerform == 2:
        prod.showAllProducts()
        print("\nPress Enter to continue")
        msvcrt.getch()
        
    elif operationPerform == 3:
        search = int(input("Enter the ID of the product you want to search: "))
        prod.searchProduct(search)
        print("\nPress Enter to continue")
        msvcrt.getch()
    
    elif operationPerform == 4:
        search = int(input("Enter the ID of the product you want to update: "))
        prod.searchProduct(search)
        choice = int((input("What do you want to update?\n1.)Name\n2.)Price\n3.)Both\n4.)Return\nEnter (1-4): ")))
        if choice == 1:
            nameUpdate = input("Enter the updated name for the product: ")
            prod.updateProduct(search,nameUpdate,0,1)
            prod.searchProduct(search)
            print("\nPress Enter to continue")
            msvcrt.getch()
        elif choice == 2:
            priceUpdate = float(input("Enter the new price for the product"))
            prod.updateProduct(search,'',priceUpdate,2)
            prod.searchProduct(search)
            print("\nPress Enter to continue")
            msvcrt.getch()
        elif choice == 3:
            nameUpdate = input("Enter the updated name for the product: ")
            priceUpdate = float(input("Enter the new price for the product: "))
            prod.updateProduct(search,nameUpdate,priceUpdate,3)
            prod.searchProduct(search)
            print("\nPress Enter to continue")
            msvcrt.getch()
            
        elif choice == 4:
            print("Returning")
    
    elif operationPerform == 5:
        search = int(input("Enter the ID of the product you want to delete: "))
        prod.delProduct(search)
        ID -= 1
        print("The list has been updated!")
        prod.showAllProducts()
        print("\nPress Enter to continue")
        msvcrt.getch()

    elif operationPerform == 6:
        search = int(input("Enter the ID of the product: "))
        stockUpdate = int(input("Enter the updated stock of the product: "))
        prod.updateStock(search,stockUpdate)
        prod.searchProduct(search)
        print("\nPress Enter to continue")
        msvcrt.getch()
    
    elif operationPerform == 7:
        prod.salesReport()
        print("\nPress Enter to continue")
        msvcrt.getch()

        
        
        

