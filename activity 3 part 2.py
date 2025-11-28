import math   # importing the math module


# Function to print Fibonacci sequence
def cal_fibonacci(length):
    if length <= 0:
        print("Invalid length")
        return
    
    # First two Fibonacci numbers
    a, b = 0, 1
    
    if length == 1:
        print(a)
        return
    
    # Print starting values
    print(a)
    print(b)
    
    # Print the rest
    for _ in range(length - 2):
        c = a + b
        print(c)
        a, b = b, c   # move forward in the sequence


# Function to print factorial using math module
def cal_factorial(n):
    print(math.factorial(n))   # using built-in factorial


# Run the program
length = int(input("Enter length for the Fibonacci sequence: "))
cal_fibonacci(length)

n = int(input("Enter a number to calculate the factorial: "))
cal_factorial(n)
