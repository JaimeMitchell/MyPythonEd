# my version
# color = input('color ')
# if (color == 'red' or 'RED' or 'Red' or 'rED' ):
#     print('red')
# else:
#     print('not red')

# paul's version

# color=input('color: ')
# if (color == 'red' or color == 'RED' or color =='Red' or color =='rED' ):
#     print('red')
# elif (color != 'red' and color != 'RED' and color != 'Red' and color != 'rED' ):
#     print('not red')

# my version
# num = float(input('num? '))
# if (num%2==0 and num!=0):
#     print('num is even')
# if (num%2==1):
#     print('num is odd')
# if (num==0):
#     print('num is 0')

# paul's answer

# num = float(input('Num? '))
# rem=num%2
# if(rem==0 and num!=0):
#     print('even')
# elif(rem==1):
#     print('odd')
# else:
#     print('zero')

# my version

# num= float(input('num? '))
# if (num>=5 and num<=10):
#     print('your number is btwn 5 and 10')
# elif(num<5):
#     print('num less than 5')
# elif(num>10):
#     print('num is greater than 10')

# paul's version
# num= float(input('num? '))
# if(num>=5 and num<=10):
#     print('in range')
# elif(num<5 or num>10):
#     print('out of range')

num = float(input('num? '))
rem = num % 2
    
if(num > 0 and rem == 0):
    print('num pos and even')
elif(num < 0 and rem == 0):
    print('num neg and even')
elif(num > 0 and rem == 1):
    print('num pos and ood')
elif(num < 0 and rem == 1):
    print('num neg and odd')
else: print('num is 0')