import random
roster = []
num = int(input('How many students are in your class? '))
for i in range(num):
  student = {}
  first = input("Please enter student's first names: ")
  first = first.split(" ") 
  last = input("Please enter student's last names: ")
  try:
    student["names"] = f'{first[0]} {first[1]} {last}'
  except: student["names"] = f'{first[0]} {last}'
  student["id"] = random.randint(111111,999999)
  try:
    student['email'] = first[0][0] + first[1][0] + last + str(student['id'])[-3:] + '@example.org'
  except:
    student['email'] = first[0][0] + last + str(student['id'])[-3:] + '@example.org'
  roster.append(student)
  print('')
for stud in roster: 
  print("") 
  for key in stud: 
    print(f'{key}: {stud[key]}')
    print()

