
d = 30

def add(a,b,c=2):
    global d
    d = 20
    print(f"The value of a is {a}")
    print(f"The value of b is {b}")
    print(f"The value of c is {c}")
    print(f"The value of d is {d}")


def add(a,b):
    global d
    d = 10
    print(f"The value of a is {a}")
    print(f"The value of b is {b}")
    print(f"The value of d is {d}")

print(f"The value of d is {d}")
add(2,3)
print(f"The value of d is {d}")

# Output:
# The value of d is 30
# The value of a is 2
# The value of b is 3
# The value of d is 10
# The value of d is 10

# Note Go through Program Line by Line
# Since there are two add function it overwrite first one with second one.
# Logic: a = 10 then a = 20 print(a) Output: 20 it overwrites values