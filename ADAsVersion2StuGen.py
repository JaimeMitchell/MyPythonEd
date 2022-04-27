import random

names = ['ROSIE MARTINEZ', 'JOE LIU', 'SALLY SUE', 'BOB JOHNSON', 'DELIA AGHO']
roster= [] # list of dictionarys

for i in range(5):
    student = {}
    student['name'] = names[i] #iteration control variable counts thru names above
    student['id'] = random.randint(111111, 999999)
    [first,last] = names[i].split()
    student['email'] = first[0] + last + str(student['id'])[-3:] + '@example.org'
    roster.append(student)
    #print(f"name: {student['name']}\nid: {student['id']}\nemail: {student['email']}\n")

for individual in roster:                     #for each dictionary in roster
   for key in individual:                     #for each key in dictionary
       print (f'{key}: {individual[key]}')    #print each key'n'value in each dictionary.
   print('')                                  #print a space after each dictionary

