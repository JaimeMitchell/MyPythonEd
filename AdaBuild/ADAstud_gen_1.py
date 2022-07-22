import random

#step 2
names = ["ROSIE MARTINEZ",	"JOE LIU",	"SALLY SUE",	"BOB JOHNSON",	"DELIA AGHO"]

#step 3
ids = []
for i in range(5):
  ids.append(random.randint(1111,9999))

#step 4
emails = []
i = 0
for name in names:
  [first,last] = name.split(" ")
  emails.append(first[0]+last+str(ids[i])[-3:]+"@adadev.org")
  i += 1

#step 5
for i in range(5):
  print(f"name: {names[i]}")
  print(f"id: {ids[i]}")
  print(f"email: {emails[i]}\n")
