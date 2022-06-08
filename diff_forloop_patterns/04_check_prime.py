# check whether number is prime or not

def check_prime(n):
    flag = True
    for count in range(2,n):
        if n % count == 0:
            flag = False
              
    if flag == True:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")
        
                
check_prime(5)
check_prime(9)

# output
'''
5 is a prime number
9 is not a prime number
'''