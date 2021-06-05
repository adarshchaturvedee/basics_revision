'''
#Natural numbers from 1 to 25
for i in range(1,26):
    print(i,'\t',end='')
'''

'''
#Reverse from 30 to 1
for i in range(30,0,-1):
    print(i,'\t',end='')
'''

'''
#Print odd from 1 to 99
for i in range(1,100,2):
    print(i,'\t',end='')
'''

'''
#Sum of all natural numbers from 1 to 50
add=0
for i in range(1,51):
    add+=i
    print('Sum from 1 to',i,'is',add)
'''

'''
#Sum of all even numbers from 1 to 50
add=0
for i in range(2,51,2):
    add+=i
    print('Sum of even numbers till',i,'is',add)
'''

'''
#Given a number find factorial
fact=int(input('Enter number whose factorial is needed: '))
for i in range(1,fact):
    fact*=i
print(fact)
'''

'''
#Given two numbers, find a raised to b
base=int(input('Enter base value: '))
exp=int(input('Enter exponent value: '))
val=base**exp
print(base,'raised to',exp,'is',val)
'''

'''
#Multiplication table
answer = 'Y'
while(answer=='Y'):
    i=int(input('Enter a number: \n'))
    j=1
    while (j<11):
        print(i,' x ',j,' = ',i*j)
        j+=1
    answer=str(input('Do you wish to continue(Y/N)?'))
'''

'''
#Check prime or not
prime=int(input('Enter number to check if prime (from 2 onwards): '))
count=0
if prime==1:
    print('Neither prime nor composite')
else:
    for i in range(2,prime):
        if prime%i==0:
            count+=1
    if count==0: print('Prime number')
    else: print('Composite number, not prime')
'''

'''
#Primes between 1 and 100
for i in range(2,100):
    count=0
    for j in range(2,i):
        if i%j==0:
            count+=1
    if count==0: print(i)
''' 

'''
#Ask user to enter command, if command is not x, print command and keep repeating
answer=input('Enter command. To quit, type: exit:')
while (answer!='exit'):
    print('You entered',answer)
    answer=input('Enter command. To quit, type: exit:')
'''

'''
#Print 5 row triangle
for i in range(1,6):
    for j in range(0,i):
        print('*',end='')
    print('')
'''

'''
#Print centred 5 row tiangle
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end='')
    for j in range(0,(i*2)-1):
        print('*',end='')
    print('')
'''

'''
#Sum till given number
num=int(input('Enter number till which you want sum: '))
add=0
for i in range(1,num+1):
    add+=i
    print('Sum from 1 to',i,'is',add)
'''

'''
#Sum of odd and even from start to end
start=int(input('Enter number from which you want sum: '))
end=int(input('Enter number till which you want sum: '))
odd,even=0,0
for i in range(start,end+1):
    if i%2==0:
        even+=i
    else:
        odd+=i
print('Sum of even numbers till',i,'is',even)
print('Sum of odd numbers till',i,'is',odd)
'''

'''
#Count of odd numbers between two limits
start=int(input('Enter number from which you want sum: '))
end=int(input('Enter number till which you want sum: '))
count=0
for i in range(start,end+1):
    if i%2!=0:
        count+=1
print('Total odd numbers between the given limits is',count)
'''

'''
#Exponent without the ** operator
base=int(input('Enter base value: '))
exp=int(input('Enter exponent value: '))
val=1
for i in range(0,exp):
    val*=base
print('Final value is: ',val)
'''

'''
#Primes from start to end
start=int(input('Enter number from which you want primes: '))
end=int(input('Enter number till which you want primes: '))
if start==1:
    start+=1
    for i in range(start,end+1):
        count=0
        for j in range(2,i):
            if i%j==0:
                count+=1
        if count==0: print(i)
else:
    for i in range(start,end+1):
        count=0
        for j in range(2,i):
            if i%j==0:
                count+=1
        if count==0: print(i)
'''

'''
#Reverse a number
num=int(input('Enter number to reverse: '))
temp=num
exp=0
while temp!=0: #to find number of digits (exp)
    exp+=1
    temp=int(temp/(10))
while num!=0:
    temp+=(num%(10))*(10**(exp-1)) #Smallest digit left*Highest exponent left
    num=int(num/10)
    exp-=1
print(temp) #Print reverse
'''

'''
#Fibonacci series and nth Fibonacci number
n=int(input('How many Fibonacci series terms do you want?'))
a,b=0,1
print(a)
for i in range(n-1):
    print(b)
    a,b=b,a+b
print('Fibonacci number',n,'is',a)
'''
#Sum of odd and even places
