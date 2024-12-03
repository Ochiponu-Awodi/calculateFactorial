def factorial_imperative(n):      # Define a function named 'factorial_imperative' that takes one parameter 'n'
    result = 1                    # Initialize a variable 'result' to 1; this will hold the final factorial value

    for i in range(2, n + 1):     # Loop through numbers from 2 to n (inclusive)
        result *= i               # Multiply 'result' by the current number 'i'

    return result                 # Return the final computed factorial value