'''
#Simple Interest
base=float(input('Enter the principal amount: '))
rate=float(input('Enter the rate of interest: '))
duration=int(input('Enter the duration in integer years: '))
simple_interest=(base*rate*duration)/100
print('Simple interest amount is: ',simple_interest)
print('Total amount to be paid/earned over',duration,' years is ',base+simple_interest)
'''

'''
#Compound interest
base=float(input('Enter principal amount: '))
rate=float(input('Enter rate of interest: '))
compound=float(input('Enter number of times compounding is done per year: '))
duration=int(input('Enter the duration in integer years: '))
compound_interest=base*(1+((rate/100)/compound))**(compound*duration)
print('Interest paid/earned is: ',compound_interest-base)
print('Total amount to be paid/received is ',compound_interest)
'''

'''
#Celsius to Fahrenheit and vice versa
scale=input('Mention the scale you wish to convert (C/F): ')
temp=float(input('Enter the temperature value upto 2 decimal places: '))
if scale =='C':
    val=9*(temp/5)+32
    print('Converted value is ',val,' degree Fahrenheit')
elif scale=='F':
    val=5*((temp-32)/9)
    print('Converted value is ',val,' degree Celsius')
else:
    print('Error in input of scale')
'''

'''
#Odd or Even
val=float(input('Enter the integer you want to check the value for: '))
if val==0:
    print(val,'is neither even nor odd')
elif val%2==0:
    print(val,'is an even integer')
elif val%2==1:
    print(val,'is an odd integer')
else:
    print(val,'is not an integer')    
'''

'''
#From CP and SP, find profit
cost_price=float(input('Enter the cost price of the product: '))
sell_price=float(input('Enter the sell price of the product: '))
profit_percent=((sell_price/cost_price)*100)-cost_price
if profit_percent<0:
    print('Loss is ',(profit_percent*(-1)),'%')
    print('Loss value is ',cost_price-sell_price)
else:
    print('Profit is ',profit_percent,'%')
    print('Profit value is ',sell_price-cost_price)
'''
