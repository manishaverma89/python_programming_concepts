NumList = []

len_Numlist = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, len_Numlist + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)
print("Elements before sorting list is: ", NumList)

for i in range (0, len_Numlist):
    for j in range(i + 1, len_Numlist):
        if(NumList[i] > NumList[j]):
            temp = NumList[i]
            NumList[i] = NumList[j]
            NumList[j] = temp
            print(NumList)         #for  testing

print("Element After Sorting List in Ascending Order is : ", NumList)


# output
'''
Elements before sorting list is:  [5, 3, 0, 1, 4, 2]
[3, 5, 0, 1, 4, 2]
[0, 5, 3, 1, 4, 2]
[0, 3, 5, 1, 4, 2]
[0, 1, 5, 3, 4, 2]
[0, 1, 3, 5, 4, 2]
[0, 1, 2, 5, 4, 3]
[0, 1, 2, 4, 5, 3]
[0, 1, 2, 3, 5, 4]
[0, 1, 2, 3, 4, 5]
Element After Sorting List in Ascending Order is :  [0, 1, 2, 3, 4, 5]



'''