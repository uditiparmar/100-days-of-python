# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

hightest_score = 0
for score in student_scores:
  if score > hightest_score:
   hightest_score = score
print(f"The highest score in the class is: {hightest_score}")
