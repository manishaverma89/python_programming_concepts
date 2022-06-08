i=1
while i<=5:
    space =1 
    while space <= 5-i:
        print(" ", end = "")
        space = space+1
    j=1
    while j <=i:
        print("*", end = "")
        j += 1
    print()
    i += 1
    
# output
'''
    *
   **
  ***
 ****
*****


'''