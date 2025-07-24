fruit_basket = ["apple", "banana", "mango", "05-dragonfruit", 5, 8] # Defining List and can contain multiple data-types.

print(fruit_basket)
print(fruit_basket[0])   # Accessing List
print(fruit_basket[1])
print(fruit_basket[2])
print(fruit_basket[3])
print("######### Negative Index ############")
print(fruit_basket[-4])
print(fruit_basket[-3])
print(fruit_basket[-2])
print(fruit_basket[-1])

# ["apple", "banana", "Mango", "Dragonfruit"]
#    0         1         2           3  ------> Index
#   -4        -3        -2          -1  ------> Negative Index

#  A  P  P  L  E
#  0  1  2  3  4   ---> Index
# -1 -2 -3 -4 -5

print("######################################")
# Syntax list[start : end : step]
# - start: Where to begin (default is 0)
# - end: Where to stop (default is end of list)
# - step: How many items to skip

print(fruit_basket[1:3]) # Range Index - banana , mango (n -3)
print(fruit_basket[-1])
print(type(fruit_basket[-1]))
print(fruit_basket[:6])
print(fruit_basket[0][3]) # it will read apple and get me index value of 3 which is "l"

print(fruit_basket[1])
print(fruit_basket[1][3])
print(fruit_basket[1][3] + " " + fruit_basket[2])

#a = ["apple", "banana", "mango", "05-dragonfruit", 5, 8]
#del a # This will delete the memory location of a
#print(a) # since its deleted the memory of a error: a not defined
