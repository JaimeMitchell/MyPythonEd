"""
1. PRINT:  Create PRINT code block at bottom of program, All input will be concatenated here.
           Must loop through each list to pull out student info and OUTPUT it in the proper order. 
           THINKING ABOUT THE ORDER I WANT MY OUTPUT TO ME helps me understand HOW TO STRUCTURE MY INPUT! 
           Starting from the input first had me driving blind. This is what I learned. Sometimes start at the end of the story:
           
           STUDENT [0], ID [0], EMAIL [0] then print STUDENT [1], ID [1], EMAIL [1]

2. NAMES:  FOR loop for INPUT first (object variable) name and last (object variable) name, concatenated as one main object in student_name list 
           Don't append seperately, will get this --> 'Jaime', 'Mitchell' instead of 'Jaime Mitchell'. We want one object made of two separate variables. 

3. ID:  FOR loop for ID random_randint(). 

4. EMAIL: The crux is I needed to turn the integers from the id into a string.  
          Within the stud_name FOR loop begin concatenation, 
          first initial of first name from stud_name[0]first[0],
          then concatenate full last name from stud_name[0]last,
          then concatenate last 3 digits of ID [], range(-3:-1)
          then concatenate "@example.com"
          
veggies = ["carrot", "yam", "zucchini", "spinach"]
for i in range (len(veggies)): 
  if len(veggies[i]) > 5:
    print(f"I love {veggies[i]}")
"""
import random

#stud_names = ['jaime mitchell', 'maria Cookoo sabina', 'tracy chapman', 'ada addie lovelace', 'lisa simpson']

#Name loop
num = int(input('How many students would you like to register? '))
stud_names = []
for i in range(num): #name and email loop
  first = (input("Please enter student's first name: ")) # first name
  first = first.split(" ")
  last = (input("Please enter student's last name: ")) # last name
  try:
    stud_names.append(f'{first[0]} {first[1]} {last}') #works but now I need to deal with making the email
  except:
    stud_names.append(f'{first[0]} {last}')  
print(stud_names)
# ID loop
stud_id = []
for i in range(num):
  id = random.randint(111111,999999)
  for i in range(num):
    id = str(id)
  stud_id.append(id)
print(stud_id)
email_list = []
for i in range(num):
  try:
    email= first[0][0]+first[1][0]+last+stud_id[i][-3:]+'@example.org'
    email = str(email)
    email_list.append(email)
  except:
    email= first[0][0]+last+stud_id[i][-3:]+'@example.org'
    email = str(email)
      
print(email_list)
