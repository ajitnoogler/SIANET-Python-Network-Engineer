a = ["Dhiraj", 1,3.0] # List stores references to the elements' memory locations.

# Dhiraj, 1, 3.0
#    0   , 1, 2
#   -3   ,-2,-1

print(a)

print(a[0]) # Dhiraj is on index 0 of the list "a"
print(a[1])
print(a[2])

print("######Negative-Index#######")
print(a[-1])
print(a[-2])
print(a[-3])


print("########List-Slicing-Elements#######")

print(a[0:2])   # [0: n-1]

print(a[0][3])  # to print "r" from Dhiraj
print(a[0][2:6]) # to print "iraj" from Dhiraj

# D, h, i, r, a, j
# 0, 1, 2, 3, 4, 5
#-6,-5,-4,-3,-2,-1

print(a[0][3:6] + " "+ str(a[1])) # accessing two elements from list and concatenate with type casting.
print(a[0][3] + str(a[1]))



print("###########List-Modify-Elements##########")

print(f"Before Modifying List: {a}")
a[0] = "SIA"
print(f"After Modifying List: {a}")



print("###########List-Delete-Elements##########")

a = ['Apple', 'Mango', 'Banana', 'Cherry', 'Blue-berry']
print(f"Before deleting elements range from the List: {a}")
del a[1:3]  # this will delete mango and banana from the list.
print(f"After deleting elements range from the List: {a}")


a = ['Apple', 'Mango', 'Banana', 'Cherry', 'Blue-berry']
print(f"Before deleting element List: {a}")
del a[2] # This will remove Banana from the list
print(f"After deleting element List: {a}")


# 'del' removes the reference of the element from the list.
# Actual memory is freed automatically by Python's garbage collector if no references exist.

#Memory effect: del a[2]
#    List a still exists.
#    Only reference to 3.0 is removed.

# Memory effect: del a
#    The list a itself is gone.
#    All references to its elements are removed.
#    If elements are not referenced elsewhere, they are also freed from memory.



print("###########Empty-List-Elements##########")

l = []
print(type(l))

R = list(range(1,10))
print(R)

Odd = list(range(1,10,2))
print(f"Odd numbers are: {Odd}")

Even = list(range(0,10,2))
print(f"Even numbers are: {Even}")

# range(start, stop, step) syntax:
#
#     start → where the sequence begins (inclusive)
#     stop → where the sequence ends (exclusive, not included)
#     step → the gap between each number

# Your code explanation:
#    start = 1 → sequence starts at 1
#    stop = 10 → goes up to 10 but does not include 10
#    step = 2 → adds 2 each time




print("###########Append-Elements-Into_List##########")
fruits = ['apple', 'Banana', 'Cherry']
print(f"Before Append Fruits List is: {fruits}")
fruits.append("Mango")
print(f"After Append Fruits List is: {fruits}") # Append only one Elements at the ends of the list

l=list()
print(l) # [] - This is Empty List
l.append(input("Enter the Element to add in List: "))
print(l)



print("###########Extend-Elements-Into_List##########")

fruits = ['apple', 'Banana', 'Cherry']
print(f"The Fruits list Before extend is: {fruits}")
fruits.extend(["Dragonfruit","Mango",2,4])  # Add more than one elements in List
print(f"The Fruits list post extend is: {fruits}")




print("###########Insert-Elements-Into_List##########")
fruits = ['apple', 'Banana', 'Cherry']
print(f"The Fruits list Before insert is: {fruits}")
fruits.insert(1,"mango") # inserting user desire element at specific index of the List
print(f"The Fruits list After insert is: {fruits}")




print("###########Remove-Elements-Into_List##########")
fruits = ['apple', 'mango', 'Banana', 'Cherry']
print(f"The Fruits list Before remove is: {fruits}")
fruits.remove("mango")
print(f"The Fruits list after remove is: {fruits}")



print("###########PoP-Elements-Into_List##########")
fruits = ['Apple', 'Mango', 'Banana', 'Cherry', 'Blue-berry']
print(f"The Fruits list Before PoP is: {fruits}")
fruits.pop() # if you dont mention anything in () it removes last elements from list
print(f"The Fruits list after PoP() is: {fruits}")

fruits.pop(2) # here i mention index of banana which is 2 and it removes banana from list
print(f"The Fruits list after PoP is: {fruits}")
print(fruits)
x = fruits.pop(2)
print(x) # this print the element which was pop out of the list fruits

print("############Summary################")
fruits = ['Apple', 'Mango', 'Banana']

fruits.append("Cherry")
fruits.extend(["Blue-Berry",3,4,5])
print(fruits)
fruits.insert(1,"Jamun")
print(fruits)
fruits.remove("Blue-Berry")
print(fruits)

del fruits[3]
print(fruits)

fruits.pop(1)
print(fruits)



print("############Length-List################")
fruits = ['Apple', 'Mango', 'Banana', 'Cherry', 'Blue-berry']
print(len(fruits))



print("############Count-List################")
fruits = ['Apple', 'Mango', 'Banana', 'Cherry', 'Banana',  'Blue-berry']
print(fruits)
print(fruits.count("Banana")) # Its counting How many time Banana is there in list



print("############Clear-List################")
fruits = ['Apple', 'Mango', 'Banana', 'Cherry', 'Blue-berry']
fruits.clear() # it will empty the list []
# here, difference between clear and del is clear returns empty list whereas del delete memory reference of list.
print(fruits)



print("############Sort-List################")
ip_address = ['192.168.1.10',
              '192.168.1.20',
              '192.168.1.14',
              '192.168.1.16',
              '192.168.1.18']

ip_address.sort(reverse=False)
print(ip_address)


fruits = ['Apple', 'Mango', 'Banana', 'Cherry', 'Blue-berry', 'Banana', 'Cherry']
fruits.sort(reverse=False)
print(fruits)



print("############-Reverse-List################")
ip_address = ['192.168.1.10',
              '192.168.1.20',
              '192.168.1.14',
              '192.168.1.16',
              '192.168.1.18']
ip_address.reverse()
print(ip_address)

fruits = ['Apple', 'Mango', 'Banana', 'Cherry', 'Blue-berry', 'Banana', 'Cherry']
fruits.reverse()
print(fruits)


print("############Copy-List################")
fruits = ['Apple', 'Mango', 'Banana', 'Cherry', 'Blue-berry', 'Banana', 'Cherry']

fruits_2 = fruits.copy()
print(fruits_2)

fruits_3 = fruits[1:4].copy()
print(fruits_3)

print(id(fruits))
print(id(fruits_2))
print(id(fruits_3))


print("############-Nested-List-################")

l2 = [1,2,3,4,[5,6,7],4,3,[9,"Dhiraj","SIA"],56,7.9,['d','p','c']]
print(l2[7][1][2])
print(l2[7][1][3:6])

