a = 300
b = 400
c = "Tons"
price = 1.33
quantity = 5
total_cost = price * quantity

print("---------Old way for formatting strings before f-string------------\n")
print("-------------------------------------------------------------------")
print("Total cost is:", total_cost)  # This will print the total cost of the items
print("The Price is %f" %total_cost)  # This will print the total cost as a floating-point number - Old way before f-string formatting
print("-------------------------------------------------------------------")
print("The Price is %s and total cost is %s" %(price, total_cost))  # This will print the price and total cost as strings - Old way before f-string formatting
print("The Price is %s and total cost is %s" %(price, price * quantity))  # This will print the price and total cost as strings - Old way before f-string formatting
print("The Price is {0} and total cost is {1} !!!".format(price,price*quantity) ) # This will print the price and total cost using format method - Old way before f-string formatting
print("-------------------------------------------------------------------\n") # \n is used to print a new line


print("----f-String is always Recommended for new way of formatting strings----------\n")
print(f"The Price is {price} and total cost is {total_cost}")  # This will print the price and total cost using f-string formatting
print("-------------------------------------------------------------------")
print(f"How much total quantity is there?", (str(a) + c) ) # This will print the quantity and the unit (Tons) using f-string formatting
print("-------------------------------------------------------------------")
print(f"How much total quantity is there? {a} {c}" ) # This will print the quantity and the unit (Tons) using f-string formatting
print("-------------------------------------------------------------------")
