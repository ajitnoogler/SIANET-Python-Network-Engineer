d =30

def add(a,b,c):
    d=20
    print(f"The value of a is {a}")
    print(f"The value of b is {b}")
    print(f"The value of c is {c}")
    print(f"The value of d is {d}")


print(f"The value of d is {d}")

add(4,5,6)

print("####################Lambda way ##############################")

val = lambda a,b,c: a*b*c
print(val(4,5,6))
