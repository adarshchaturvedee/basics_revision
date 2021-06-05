'''
count=0
for i in range(1,5):
    for j in range(i):
        count+=1
        print(count,end='')
    print('')
'''

'''
a=int(input('Number of rows needed: '))
for i in range(1,a):
    if(i==1):
        print(i)
    else:
        print(i,end='')
        for j in range(0,i-2):
            print('0',end='')
        print(i)
'''

'''
1
11
121
1331
14641
15101051
'''

'''
a,b=0,1
print(a)
for i in range(2,5):
    for j in range(i):
        print(b,end='')
        a,b=b,a+b
    print('')
'''

'''
for i in range(1,4):
    for j in range(4,i+1,-1):
        print(' ',end='')
    for k in range(5-i,4+i):
        print('*',end='')
    print('')    
for i in range(1,3):
    for j in range(i):
        print(' ',end='')
    for k in range(i,5-i):
        print('*',end='')
    print('')
'''

'''
for i in range(3):
    for j in range(i,3):
        print('*',end='')
    for j in range(3-i,3+i):
        print(' ',end='')
    for j in range(i,3):
        print('*',end='')
    print('')    
for i in range(2,4):
    for j in range(i):
        print('*',end='')
    for j in range(i,6-i):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    print('')
'''      

'''
for i in range(1,5):
    for j in range(4-i):
        print(' ',end='')
    for j in range(i,2*i):
        print(j,end='')
    for j in range((2*i)-2,i-1,-1):
        print(j,end='')
    print('')
'''

'''
for i in range(1,4):
    for j in range(i,3):
        print(' ',end='')
    for j in range(i,(2*i)):
        print(j,end='')
    for j in range(2*i-2,i-1,-1):
        print(j,end='')
    print('')
for i in range(1,3):
    for j in range(1,i+1):
        print(' ',end='')
    for j in range(3-i,6-(2*i)):
        print(j,end='')
    for j in range(i+1,3):
        print(j,end='')
    print('')
'''

'''
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end='')
    for j in range(1,(2*(4-i))):
        print(' ',end='')
    if i!=4:
        for j in range(i,0,-1):
            print(j,end='')
        print('')
    else:
        for j in range(i-1,0,-1):
            print(j,end='')
        print('')
'''
