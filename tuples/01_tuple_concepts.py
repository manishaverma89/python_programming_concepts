# Update tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print (x)


# Append to tuple
a = ("apple", "banana", "orange")
b = list(a)
b.append("kiwi")
print (tuple(b))


# Add tuple to a tuple 
# Allowed to add tuple to a tuple
first_tuple = ("a","b", "c")
new_tuple = ("d",)
first_tuple += new_tuple
print (first_tuple)


# Remove items from tuple
first_tuple = ("x", "y", "z")
new_tuple = list(first_tuple)
new_tuple.remove("y")
print(tuple(new_tuple))


# Unpacking a Tuple
fruits = ("banana", "apple", "peach", "strawberry")
(a, b, c, d) = fruits
print(a)
print(b)
print(c)
print(d)


# Using Asterisk (*)
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:


fruits = ("banana", "apple", "peach", "strawberry")
(a, b, *c) = fruits
print(a)
print(b)
print(c)


# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


# Loop Through a Tuple
names = ("manisha", "bhavya", "atharv")
for name in names:
    print(name)
    

# Loop Through the Index Numbers
names = ("manisha", "bhavya", "atharv", "aarav")
for name in range(len(names)):
    print(names[name])
    
    
# Using a While Loop
names = ("manisha", "bhavya", "atharv", "aarav", "prince", "harsh")
name = 0
while name < len(names):
    print (names[name])
    name +=1
    
# Join Two Tuples
tuple_01 = ("a", "b", "c")
tuple_02 = (1 ,2 ,3)
tuple_03 = tuple_01 + tuple_02
print(tuple_03)


# Multiply tuples
tuple1 = (1, 2, 3, 4)
tuple2 = tuple1 * 3
print(tuple2)


# tuple methods
# count() method
tuple1 = (1, 2, 3, 4)
tuple2 = tuple1 * 3
print(tuple2.count(2))
print(tuple1.count(4))

# index() method
# It returns first occurrence of the element in the tuple.
tuple1 = (1, 2, 3, 4)
tuple2 = tuple1 * 3
print("Index of 3 is:", tuple2.index(3))
print("Index of 1 is:", tuple2.index(1))
print("Index of 2 is:", tuple2.index(2))

