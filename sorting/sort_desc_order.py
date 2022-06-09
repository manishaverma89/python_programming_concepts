numlist = [3,6,9,2,10]
print("Original list is: ", numlist)

for i in range(0, len(numlist)):
    for j in range(i+1, len(numlist)):
        if numlist[i] < numlist[j]:
            temp = numlist[i]
            numlist[i] = numlist[j]
            numlist[j] = temp
            print(numlist)   # It will print All iterations
print("Elemnts in descending order are: ", numlist) 