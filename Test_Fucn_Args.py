# A function call means you're executing the function to run the code inside it.
# The return keyword sends a result back from the function to wherever it was called.
# Arguments are those, if you want to send data from caller to the function defination
#    - Required Arguments
#    - Keyword Arguments
#    - Default Arguments
#    - *args && *kargs
#=========================================================================
# Example of Default Arguments:

def add(a,b,c):
    print(f"The value of a is {a}")
    print(f"The value of b is {b}")
    print(f"The value of c is {c}")

add(1,2,3)
add(*map(int, input("Enter 3 numbers with space: ").split()))

#=========================================================================
# Arg -> Function
# Why Like this:- add(*map(int, input("Enter 3 numbers with space: ").split()))
#_________________________________________________________________________________________________________
# | Code                        | Valid? | Why                                                            |
# | --------------------------- | ------ | ---------------------------------------------------------------|
# | `map(int, input().split())` | ✅      | Applies `int` to each element of the list                     |
# | `map(int(input().split()))` | ❌      | Tries to convert the whole list to `int()` first, which fails |

# input("Enter...").split()           # ➜ returns a list of strings
# map(int, [...])                     # ➜ applies int() to each string
# *map(...)                           # ➜ unpacks the mapped integers into the function
# add(a, b, c)                        # ➜ gets the 3 unpacked numbers