
d = 30
print("++++++++++++++++++++++++++++++++++++")
def add(a,b,c):
    global d
    d = 20
    print(f"The value of a is {a}")
    print(f"The value of b is {b}")
    print(f"The value of c is {c}")
    print(f"The value of d is {d}")

print(f"The value of d is {d}")

add(a=3,b=4,c=5) # Keyword argument

print(f"The value of d is {d}")


# from inside Function it can access outside variable
# but from outside you cannot access variable inside function.
# global is need inside function to make variable accessible to outside.
# hence used global d in add()
