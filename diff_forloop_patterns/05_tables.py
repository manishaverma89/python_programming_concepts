# Print Tables of 4 and 5

for num in range(4,6):
    print(f"Table for {num} is:")
    for count in range(1,11):
        c = num * count
        print (num, " X " ,count, " = ", c)
    
    if count == 10:   
        print()
          
           
 #output
'''
 Table for 4 is:
4  X  1  =  4
4  X  2  =  8
4  X  3  =  12
4  X  4  =  16
4  X  5  =  20
4  X  6  =  24
4  X  7  =  28
4  X  8  =  32
4  X  9  =  36
4  X  10  =  40

Table for 5 is:
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50

 
''' 
        
        
        