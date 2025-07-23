def add(a,b,c):
    print(f"The value of a is {a}")
    print(f"The value of b is {b}")
    print(f"The value of c is {c}")

add(a=3,b=4,c=5) # Keyword argument
add(*map(int, input("Enter 3 numbers with space: ").split()))
