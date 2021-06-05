#Hello World
#print ('Hello World')

'''
#String input and print with concatention
a = str(input('What is your name?\n'))
print('Hi '+a+'!')
'''

'''
#Basic math
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c,d,e,f,g=a+b,a-b,a*b,int(a/b),a%b
print("Sum is ", c)
print("Difference is ", d)
print("Product is ", e)
print("Quotient is ", f)
print("Remainder is ", g)
'''

'''
#Inc triangle
for i in range(1,5):
    for j in range(0,i):
        print('*',end='')
    print('')
'''

'''
#Dec triangle
for i in range(5,1,-1):
    for j in range(1,i):
        print('*',end='')
    print('')
'''

'''
#Inc triangle reverse
for i in range(1,5):
    for j in range(i,4):
        print(' ',end='')
    for k in range(i,0,-1):
        print('*',end='')
    print('')
'''

'''
#Dec triangle reverse
for i in range(0,5):
    for j in range(0,i):
        print(' ',end='')
    for k in range(i,4):
        print('*',end='')
    print('')
'''

'''
#Diamond star
for i in range(1,9):
    for j in range(9,i+1,-1):
        print(' ',end='')
    for k in range(10-i,9+i):
        print('*',end='')
    print('')    
for i in range(1,9):
    for j in range(0,i):
        print(' ',end='')
    for k in range(i,15-i):
        print('*',end='')
    print('')
'''

'''
#Diamond space
for i in range(0,10):
    for j in range(i,10):
        print('*',end='')
    for k in range(9-i,9+i):
        print(' ',end='')
    for j in range(i,10):
        print('*',end='')
    print('')    
for i in range(2,11):
    for j in range(0,i):
        print('*',end='')
    for k in range(i,20-i):
        print(' ',end='')
    for j in range(0,i):
        print('*',end='')
    print('')
'''      
