# your code goes here
'''
a main list stud_roster composed of dictionaries called stud_info (len is 3)
Loop to create stud_info dictionaries: 
start with input "How many students", this number dictates amount of dictionaries required
1. loop: input "Student's names? :"
    1. nested loop: email- first initial, last names, ID function last 3 digits + @example.org
        a. conditional for first names with space?? 
        b. space for last name after after first name. Or vise versa whole name dealt with and then first name?
        c. I realized that the if else wasn't working to print both kinds of first name, single and double, so maybe two SEPERATE if statements?
          try using pass or break if creating nested loops to test for correct first name to be appended to email
2. Print stud-roster list outside of main loop. If in main loop must be hardcoded
'''


import random
import re
roster = []
num = int(input('How many students are in your class? '))
for i in range(num):
  names = [] #needs to be in loop to reset 
  student = {}
  first = str(input("Please enter student's first names: "))
  #if " " in first:
  first = first.split(" ") #MUST REASSIGN VALUE TO ITSELF
  names.append(first)
  last = str(input("Please enter student's last names: "))
  names.append(last)
  names = str(names) #Must Reassign list to string in order to use split. For whatever reason, Ada's split solution doesn't work when user inputs name. 
  names.split(" ")
  student["names"] = names
  print(names)
  student["ID"] = random.randint(111111,999999)
  email = []
  
  email.append(first[0][0] + first[1][0] + last + str(student["ID"])[-3:]+'@example.org')
  
  student["email"] = email
  roster.append(student)
  print(f'{roster[i]}')
