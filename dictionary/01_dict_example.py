prog_dictionary = {
    "Bug": "bug value",
    "function": "function value",
    123: "number value"
}

# Retrieving items from dictionary
print(prog_dictionary[123])   # it will print the value of bug

# Adding items to dictionary
prog_dictionary["234"] = "another number value"
print(prog_dictionary)

# create an empty dictionary
empty_dict = {}

# Wipe an existing dictionary
# prog_dictionary = {}
# print(prog_dictionary)

# Edit an item in a dictionary
prog_dictionary["Bug"] =  "An error in a program"
print(prog_dictionary)

# Loop through a dictionary
for key in prog_dictionary:
    print(key)                     # Prints the key
    print(prog_dictionary[key])    # Print the value based on the key

