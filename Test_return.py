def cube():
    a = 3
    return a * a * a  # Computes and returns the cube of 'a'

print(cube())  # Calls cube(), prints the returned result (27)

x = cube()     # Calls cube(), stores the result (27) in variable x
print(x)      # Prints the value stored in x

# return, return the results and caught by cube() & displayed by print

# Function return value -> Caller
# A function is a block of reusable code that performs a specific task.
# You define it once and can use it multiple times
# like a mini-program inside your main program.

# Why Use Functions?
#   To avoid repeating code
#   To organize logic clearly
#   To make code easier to test and debug

# A function is like a coffee machine:
#    You give input (water +:22 coffee beans)
#    Press a button (function call)
#    It gives you coffee (output)

# A function call means you're executing the function to run the code inside it.
# The return keyword sends a result back from the function to wherever it was called.
# Arguments are those, if you want to send data from caller to the function definition
#    - Required Arguments: Mandatory
#    - Keyword Arguments:
#    - Default Arguments:
#    - *args && *kargs  :