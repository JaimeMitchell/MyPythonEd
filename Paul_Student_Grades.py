numGrades = int(input("How many grades: "))
grades = []
sum = 0
highgrade = 0
for i in range(0,numGrades,1):
    grade = float(input("grade: "))
    grades.append(grade)
print(grades)
for i in range(numGrades):
    print(grades[i])
for i in range(0,numGrades,1):
    sum += grades[i]
average = sum/numGrades
for i in range(numGrades):
    if grades[i] > highgrade:
        highgrade = grades[i]


print(sum)
print(average)
print(highgrade)