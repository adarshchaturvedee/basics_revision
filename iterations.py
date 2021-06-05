'''
#If Else with While (Recursive Calculator)
answer = 'Y'
while(answer=='Y'):
    a=int(input("Enter first integer: \n"))
    b=int(input("Enter second integer: \n"))
    c=str(input("Enter operator: +, -, *, /, %, **, //: \n"))
    if (c == '+'):
        d=a+b
        print(d)
    elif (c == '-'):
        d=a-b
        print(d)
    elif (c == '*'):
        d=a*b
        print(d)
    elif (c == '/'):
        d=a/b
        print(d)
    elif (c == '%'):
        d=a%b
        print(d)
    elif (c == '**'):
        d=a**b
        print(d)
    elif (c == '//'):
        d=a//b
        print(d)
    else:
        print("Wrong operator!")
    answer=str(input("Do you wish to continue(Y/N)?"))
'''

'''
#While Loop (Create a recursive multiplication table)
answer = 'Y'
while(answer=='Y'):
    i=int(input("Enter a number: \n"))
    j=1
    while (j<11):
        print(i," x ",j," = ",i*j)
        j+=1
    answer=str(input("Do you wish to continue(Y/N)?"))
'''

'''
#For loop
n=int(input("How many Fibonacci series terms do you need?"))
a,b=0,1
print(a)
for i in range(n-1):
    print(b)
    a,b=b,a+b
'''

'''
#Nested For loop pattern generation
for i in range(0,10):
    for j in range(0,i+1):
        print('*',end='')
    print('')
'''

'''
#Loop with row number in the beginning and end and zeroes in between
a=int(input("How many rows do you need: "))
for i in range(1,a):
    if(i==1):
        print(i)
    else:
        print(i,end='')
        for j in range(0,i-2):
            print('0',end='')
        print(i)
'''
