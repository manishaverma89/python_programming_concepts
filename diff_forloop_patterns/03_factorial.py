# find factorial of a number
#  n! = n * (n-1) * (n-2) * (n-3) * (n-4) * - - - -- --  1

def factorial(n):
    
    fact = 1
    for count in range(1, n+1):
        fact = fact * count
        count = count + 1
    print("factorial is:", fact)
    
factorial(5)

# output
'''
factorial is: 120

'''