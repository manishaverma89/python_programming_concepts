# find highest student score using for loop

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# one way of finding the highest score is using max() method
# max(student_scores)

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"highest score is: {highest_score}")
  



