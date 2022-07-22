import pickle
with open('program1.pkl', 'rb') as rf:
    numStudents = pickle.load(rf)
    names = pickle.load(rf)
    grades = pickle.load(rf)

while (1 == 1):
    name = input('Who? ')
    for i in range(0, numStudents, 1):
        if (names[i] == name):
            print(f'{name}\'s grade is {grades[i]}')
