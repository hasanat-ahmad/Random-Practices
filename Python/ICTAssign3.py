def calcFinal(n):
    startPrice = discPrice = n
    discount = 0
    deduction = 0
    days = {0:"Monday",1:"Tuesday", 2: "Wednesday",3: "Thursday", 4: "Friday"} # Assigning days of the weeks to numbers
    for i in range (5):
        discount = 0.1
        
        if i > 1:                           # Special discounts
            if i == 2 and discPrice < 50:
                discount += 0.05
            elif i == 3 and (discPrice >= 50 and discPrice < 100):
                discount += 0.08
            elif i == 4 :
                if discPrice > 100:
                    discount += 0.15
        discPrice -= discPrice*discount
        if i == 4 and discPrice < 10:  # 2 dollars special discount if less than 10
            discPrice -= 2
        print(f"The discounted price on {days[i]} will be ${discPrice:.2f}")
        
        
        
        
            
    
    


iniPrice = float(input("Enter a price: "))
calcFinal(iniPrice)

    