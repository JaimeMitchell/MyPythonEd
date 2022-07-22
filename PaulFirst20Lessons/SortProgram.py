# Variables
grades = []
average = float
sum = 0
lowGrade = 100
highGrade = 0


# Number of Grades
numGrade = int(input('how many grades? '))

# Average
for grade in range(0, numGrade, 1):
    grade = float(input('grade? '))
    grades.append(grade)
for i in range(0, numGrade, 1):
    sum += grades[i]
average = sum / numGrade

# Get High & Low Grade
for i in range(0, numGrade, 1):
    if (grades[i] > highGrade):
        highGrade = grades[i]
    if (grades[i] < lowGrade):
        lowGrade = grades[i]


# Lists from array [grades*n]
for i in range(0, numGrade-1, 1):
    print(f'1ST FOR-LOOP iteration {i +1}')
    print(grades)
    
    for i in range(0,numGrade-1,1):
        swap = grades[i]
        print(f'2ND-FOR LOOP iteration {i +1}')
        print(grades)
        print(swap)
       
        if grades[i] < grades[i + 1]:
        
            grades[i] = grades[i+1]
        
            grades[i + 1] = swap
            print(f'Ran the IF-STATEMENT iteration {i +1}')
            print(grades)
            print(swap)
        

print('LAST PRINT OUTSIDE OF LOOPS')
print(grades)
print(swap)
   

    # Print
print(f'The student\'s average is {average}')
print(f'The student\'s High Grade is {highGrade}')
print(f'The student\'s Low Grade is {lowGrade}')
if(numGrade == 1):
    print(f'the student\'s {numGrade} grade is:')
else:
    print(f'the student\'s {numGrade}s grades are:')
for i in range(0, numGrade, 1):
    print(grades[i])
