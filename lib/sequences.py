#!/usr/bin/env python3
def print_fibonacci(length):
    if length <= 0:
           print([])
           return
    # Initialize the Fibonacci sequence
    fib_array = [0, 1]
    
    # Print the initial values based on the required length
    if length == 1:
        print([0])
        return
    elif length == 2:
        print([0, 1])
        return
    
    # Generate the Fibonacci sequence up to the desired length
    for i in range(2, length):
        next_number = fib_array[-1] + fib_array[-2]
        fib_array.append(next_number)
    
    # Print the Fibonacci sequence
    print(fib_array)


    

    