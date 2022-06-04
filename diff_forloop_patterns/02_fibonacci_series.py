
def fibonacci(n):
    first_no = 0
    second_no = 1
    print(first_no)
    print(second_no)
    
    for count in range (2,n):
        next_no = first_no + second_no
        print(next_no)
        first_no = second_no
        second_no = next_no
        count = count+1 
    
fibonacci(15)    
