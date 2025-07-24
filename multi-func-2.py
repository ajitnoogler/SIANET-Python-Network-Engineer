d = 30

def add(a,b,c=2):
    global d
    d = 20
    print(f"The value of a is {a}")
    print(f"The value of b is {b}")
    print(f"The value of c is {c}")
    print(f"The value of d is {d}")


def add1(d):
    return d**2

print(f"The value of d is {d}") # 30
add(2,3) # 2 - 3 - 2 - 20

print(f"The value of d is {d}") # 20
sq=add1(4)

print(f"The vaule of Square is {sq}") #16