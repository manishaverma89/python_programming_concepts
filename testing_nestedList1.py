nestedList = [1, 2, ['a', 1], 3]

# indexing list: the sublist has now been accessed
subList = nestedList[2]

# access the first element inside the inner list:
element = nestedList[2][0]

print("List inside the nested list: ", subList)   # gives output: ['a', 1]
print("First element of the sublist: ", element)  # gives output:  a