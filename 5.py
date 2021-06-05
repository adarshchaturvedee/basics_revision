from functools import reduce
'''
cms=[10,100,0,-5]
valid_cms=list(filter(lambda x: x>=0,cms))
print(valid_cms)

cms_to_m=list(map(lambda x: x/100, valid_cms))
print(cms_to_m)

total_sum=reduce(lambda x,y: x+y, cms_to_m)
print(total_sum)

list1=sum([x/100 for x in cms if x>=0])
print(list1)

arey=[6,5,8,3,9,3,6,1,9]
arey2=[9,9,7,5,2,0,2,9,8,9]
areysum=list(map(lambda x,y:x+y, arey, arey2))
print(areysum)

def factorial(x):
    if x==1:
        return 1
    return x*factorial(x-1)
print(factorial(5))

memory=[None]*1000
def fibonacci(kyun):
    if memory[kyun]!=None:
        return memory[kyun]
    if kyun==0 or kyun==1:
        return kyun
    result = fibonacci(kyun-1)+fibonacci(kyun-2)
    memory[kyun]=result
    return result
print(fibonacci(338))

def pawar(x,y):
    if y==0:
        return 1
    return x*pawar(x,y-1)
print(pawar(2,40))
'''

def power(x,y):
    if y==0: return 1
    if y<0: return 1/(power(x,abs(y)))
    partial=power(x,y//2)
    if y%2==0:
        return partial**2
    else:
        return x*((partial)**2)
print(power(2,-1))

def numPaths(r,c):
    if r==0 or c==0:
        return 0
    if r==1 and c==1:
        return 1
    if r==2 and c==2:
        return 0
    return numPaths(r-1,c)+numPaths(r,c-1)
print(numPaths(3,3))






    
