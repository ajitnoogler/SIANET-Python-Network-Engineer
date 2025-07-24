# The variable in program may not accessible at all location
# in that program. This depend on where you have declared var

# The scope of a variable determines the portion of the program
# where you can access a particular identifier
# Two Scopes: Global Variable and Local Variable.

def add(a,b,c,d):
    print(f"The value of a is {a}")
    print(f"The value of b is {b}")
    print(f"The value of c is {c}")
    print(f"The value of d is {d}")
add(a=3,b=4,c=5,d=8) # Keyword argument
add(*map(int, input("Enter 4 numbers with space: ").split()))


