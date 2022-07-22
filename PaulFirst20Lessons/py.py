
#print(format(all_total,".2f"))

# try split ()
#try doing this to  https://stackoverflow.com/questions/19371358/python-typeerror-unhashable-type-list

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(v, i)
    print(i, v)
    
hello = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

print(hello)

for k, v in hello.items():
    print(k, v)

account = ['name', 'months', 'ad-free', 'vod', 'total']
answers = ['Account1', 2.27, 1.35, 33.33, 80.987]
for q, a in zip(account, answers):
    print('{0} {1}'.format(q, a))

func = lambda x,y,z: x + y +z
x = [6.00,27.99]
y = [6.00,27.99]
z = [6.00,27.99]

print(list(map(func,x,y,z)))


#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

#Example
#Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")

#nested dictionary example 1
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

print(input())