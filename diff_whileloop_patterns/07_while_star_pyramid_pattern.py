column_count = 9
row_count = 1
while row_count <=5:
    space = 0
    while space <= row_count:
        print(" ", end = " ")
        space += 1 
        
        
    j = 1
    while j <= k:
        print("*", end = " ")
        j = j+1
    
    k = k-2   
    print()
    row_count = row_count+1
        
# output
'''
    * * * * * * * * * 
      * * * * * * * 
        * * * * * 
          * * * 
            * 

'''