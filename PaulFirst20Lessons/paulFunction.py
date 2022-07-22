def tally(x,y):
    # x=float(input('please input your number? '))
    # y=float(input('second num '))
    z=x+y
    print('x=',x)
    print("y=",y)
    print('x+y=',z)
    return x,y,z
boo=4
haa=17
print(tally(boo,haa))

def what(num):
    x=[]
    for i in range(0,num,1):
        myNums = float(input('nums '))
        x.append(myNums)
        return x

nummy=int(input('number? '))
what(nummy)