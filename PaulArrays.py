import math
g1 = 'hello'
g2 = 'yay'
print(g1, g2)

x = 4
y = 1/2
z = x**y
print(z)


# r=C/2π
c = 4
p = 3.14
radius = c/(2*math.pi)
print(f'The radius of a circle is {radius}.')

# C=2πr=2·π·4≈25.13274
r = 4
circumference = (2*math.pi)*r
print(f'The circumference of a circle is {circumference}.')

# A=πr2=π·42≈50.26548
Area = math.pi*(r**2)
print(f'The area of a circle is {Area}.')

myArray = [1, 45, 6, 777, 'monkey']
print(myArray)
print(myArray[0])
print(myArray[-1])

print(myArray[0] + myArray[-2])

picture = [[1, 2, 3, 4],
           [5, 6, 7, 8], [9, 19, 3, 4]
           ]
print(picture[0]+picture[1])
print(picture[1][2])
picture[0][0] = 67
print(picture)
x = []
x.append(22)
x.append(98)
print(x)
x[0] = 80
print(x)

print(fruits[0])
print(fruits[1:3])
fruity = fruits[1:4]
print(fruity)  # prints new array
