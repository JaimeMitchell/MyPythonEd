import pickle

names = []
grades = []
num = int(input('number of students? '))
for i in range(num):
    name = input('name please: ')
    prompt = f'Please enter {name}\'s grade: '
    grade = float(input(prompt))
    names.append(name)
    grades.append(grade)
with open('studGrades.pkl', 'wb') as f:
    pickle.dump(names, f)
    pickle.dump(grades, f)
with open('studGrades.pkl', 'rb') as f2:
    pickle.load(f2)
    pickle.load(f2)

while i:
    n = input('Please tell me who you want: ')
    for i in range(num):
        if(n == names[i]):
            print(f'{names[i]} has an averages of {grades[i]}')
