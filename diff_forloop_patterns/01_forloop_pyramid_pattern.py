for row_count in range(1, 7):
    for column_count in range(1, row_count+1):
        print("*", end = " ")
    print()   


for row_count in range(1, 7):
    for column_count in range(7, row_count+1, -1):
        print("*", end = " ")
    print()



# output
'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

'''
        
    


