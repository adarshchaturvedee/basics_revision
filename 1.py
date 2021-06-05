'''
#Max of two numbers
int1=int(input('Enter first integer for comparison:'))
int2=int(input('Enter second integer for comparison:'))
max_of_two=int1
if int2>max_of_two:
    max_of_two=int2
print('Greater of the two numbers is:',max_of_two)
'''

'''
#Max of three numbers
int1=int(input('Enter first number for comparison:'))
int2=int(input('Enter second number for comparison:'))
int3=int(input('Enter third number for comparison:'))
max_of_3=max(int1,int2,int3)
print('Greatest of the three numbers is:',max_of_3)
'''

'''
#Positive, negative or zero
number=float(input('Enter the number to check positive, negative or zero: '))
if number==0:
    print('Number is a zero')
elif number>0:
    print('Number is positive')
else:
    print('Number is negative')
'''

'''
#YES if divisible by 5 and 11 else NO
number=int(input('Enter the number to check divisibility by 5 and 11: '))
if number==0:
    print('ZERO')
elif number%5==0 and number%11==0:
    print('YES')
else:
    print('NO')
'''

''' 
#Leap year or not and month
month_number=int(input('Enter month number from 1 to 12: '))
if month_number==2:
    year=int(input('Enter the year to check if leap or not: '))
    if year%4==0:
        if year%100==0:
            if year%400==0: print('29 days, leap year')    
            else: print('28 days, not a leap year')
        else:print('29 days, leap year')
    else: print('28 days, not a leap year')
elif month_number==4 or month_number==6 or month_number==9 or month_number==11:
    print ('30 days')
elif month_number>0 and month_number<13: print('31 days')
else: print('Wrong input')
'''

'''
#Check if character is uppercase or lowercase.Print U or L
char=input('Enter a single uppercase or lowercase character :')
upper=char.isupper()
lower=char.islower()
if upper==1: print('U')
elif lower==1: print('L')
else: print('Error')
print('ASCII comparison explicitly is boring so I used string function :-P')
'''

'''
#Minimum notes needed to reach amount
amount=int(input('Enter integer amount in multiples of fifty: '))
_2000_=int(amount/2000)
rem_2000=amount%2000

_500_=int(rem_2000/500)
rem_500=rem_2000%500

_100_=int(rem_500/100)
rem_100=rem_500%100

_50_=int(rem_100/50)

notes=_2000_+_500_+_100_+_50_
print(_2000_,_500_,_100_,_50_,notes)
#Did not understand why conditions are needed here
'''

'''
#Check if traingle can be formed, tell type. Scalene, isosceles or equilateral.
a=int(input('Enter first side of traingle:'))
b=int(input('Enter second side of triangle:'))
c=int(input('Enter third side of traingle:'))
if a+b>c and b+c>a and a+c>b:
    if a==b==c:
        print('Equilateral traingle')
    elif a==b or b==c or a==c:
        print('Isosceles triangle')
    else: print('Scalene triangle')
else: print('Traingle cannot be formed')
'''
