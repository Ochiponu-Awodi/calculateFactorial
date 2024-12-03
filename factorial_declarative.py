from functools import reduce                                 # Import the 'reduce' function from the 'functools' module

def factorial_declarative(n):                                # Define a function named 'factorial_declarative' that takes one parameter 'n'
    return reduce(lambda x, y: x * y, range(1, n + 1))       # Use 'reduce' to apply a lambda function that multiplies all numbers in the range from 1 to n (inclusive)
                                                             # 'range(1, n + 1)' generates a sequence of numbers from 1 to n