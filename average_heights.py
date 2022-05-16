# Finding average student height from a list of heights

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
 student_heights[n] = int(student_heights[n])

print(student_heights)

# print sum of student_height
# print(sum(student_heights))
# or
total_height = 0
for height in student_heights:
    total_height += height     # total_height = total_height + height
print(total_height)  

# print number of students
# print(len(student_heights))
# or

number_of_students = 0
for student in student_heights:
  number_of_students += 1     # number_of_students = number_of_students + 1
print(number_of_students) 

average_height = round(total_height/number_of_students)
print(average_height)

