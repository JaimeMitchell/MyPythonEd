# defining functions

import array


def inputGrades(num):
    ary = []
    for i in range(num):
        grade = float(input('Please input grade: '))
        ary.append(grade)
    return ary


def printGrades(num, arrayFunc, average, highLow):
    print('Your grades are: ')
    for i in range(num):
        print(arrayFunc[i])
    print(f'your average is {average}')
    j = 0
    while j < 1:
        print(
            f'your highest grade is {highLow[j]} and your lowest grade is {highLow[j+1]}.')
        j = j+1


def average(num, arrayFunc):
    sum = 0
    for i in range(num):
        sum += arrayFunc[i]
        average = sum/num
    return round(average, 1)


def highLow(num, arrayFunc):
    high = 0
    low = 100
    for i in range(num):
        if arrayFunc[i] > high:
            high = arrayFunc[i]
    for i in range(num):
        if arrayFunc[i] < low:
            low = arrayFunc[i]
    return high, low

    # assigning my argument value before passing it to functions
num = int(input('Please input amount:  '))

# invoking functions
x = inputGrades(num)
y = average(num, x)
z = highLow(num, x)
printGrades(num, x, y, z)
