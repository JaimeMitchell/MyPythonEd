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
with open('program1.pkl', 'wb') as WriteFile:
    pickle.dump(num, WriteFile)
    pickle.dump(names, WriteFile)
    pickle.dump(grades, WriteFile)
with open('program1.pkl','rb') as ReadFile:
    a=pickle.dump(ReadFile)
    b=pickle.dump(ReadFile)
    c=pickle.dump(ReadFile)