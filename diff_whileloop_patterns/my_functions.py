# Print 1-100 using while_loop 
def while_loop(number):
    print("count:\n")
    i = 1
    while i <= number:
        print(i)
        i+=1
       
       
# Print 1-100 even_numbers
def even_number(number):
    print("Even numbers are:")
    i = 1
    while i <= number:
       if i % 2 == 0:
           print(i)
       i+=1
       
# Print 1-100 odd numbers
def odd_number(number):
      print("Odd numbers are:\n")
      i = 1
      while i <= number:
          if i % 2 != 0:
              print (i)
          i+=1

        
# Print 1-100 Prime numbers
def prime_number(lower, upper):
    for num in range(lower, upper):
        if num > 1:
            for i in range(2, num):
                if(num%i) == 0:
                    break
            else:
                print(num)



        
    
    

    
        
    
            
            
