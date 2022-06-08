k = 1
i = 1
while i <= 5:
    space = 1
    while space <= 5-i:
        print(" ", end= " ")
        space = space+1
        
    j = 1
    while j <= k:
        print("*", end = " ")
        j = j+1
    
    k = k+2
    print()
    i=i+1
    
    
    
# output:
'''
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 

'''
    