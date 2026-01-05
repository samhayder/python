student_scores = [254,126,987,123,546,258,112,224,326,351,146,204]

#SUM
sum = 0
for score in student_scores:
    sum += score
print("Sum ",sum)

#Max
max_score = student_scores[0]
for i in range(len(student_scores)):
    if student_scores[i] > max_score:
        max_score = student_scores[i]
print("Max ",max_score)
print(max(student_scores))

#SUM 1-100
sum1 = 0
for i in range(1,101):
    sum1 += i
print("Sum1 ", sum1)