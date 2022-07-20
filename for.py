from contextlib import nullcontext
from stat import FILE_ATTRIBUTE_DIRECTORY


# fruits = ['apple', 'banana', 'mango', 'cherry', 'kiwi']
# print(fruits)

# for fruit in fruits:
#     print(fruit)
#     for letter in fruit:
#         print(letter)

# for i in fruits:
#     print(i)
#     for n in (i):
#         print(n)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in numbers:
#     print(i)
#     print(-i)

# counting 0 to 10. end point is exclusive so need to make it 11 to stop at 10
# for i in range(0,11,1):
#     print(i)

# # counting down 10 to 0. end point is exclusive so need to make it -1 to stop at 0
# for i in range(10,-1,-1):
#     print(i)

# listOfGrades = []
# numOfGrades = int(input('how many grades do you want to input? '))
# print(listOfGrades)

# for i in range(0, numOfGrades, 1):
#     grades = float(input('enter grade: '))
#     listOfGrades.append(grades)
#     print(listOfGrades)
# # my way of handling second for loop
# for i in listOfGrades:
#     print(i)
# # paul's way of handling second for loop
# for i in range(0, numOfGrades, 1):
#     print(listOfGrades[i])

#empty array to place grades
list=[]
#variable to hold the changing sum
sum=0
#variable to hold the value of list's mean average
average=0
#the first question we must ask the user is "how many items do you want?"
n=int(input('How many grades? '))
#we must iterated over that number of items to get specificity of what value EACH item holds.
for i in range(0, n, 1):
    #We must ask a second question n number of times.
    grade=float(input("what's the grade? "))
    # We append each number to the array.
    list.append(grade)
    #add each item to the value of sum.
    sum+=grade
    print(list)
    print(sum)
#WRITE DOWN THE ENTIRE PSEUDOCODE FIRST
average=sum/n
print(average)
#A loop to output the number on the console or window.
# for i in range(0,n,1):
#     sum/=average

#     print('The grades are: ')
#     print(list[i])
#     print('the average is: ')
# #calculate the average outside of the loops to make program run quicker
# #print the average
# print(average)
