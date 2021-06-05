'''
def fact(BC_number_hi_dena):
    if BC_number_hi_dena==0:
        return 1
    else:
        for i in range(1,BC_number_hi_dena):
            BC_number_hi_dena*=i
        return BC_number_hi_dena
fact(5)
print(fact(5))

def combo(n,r):
    return int(fact(n)/(fact(r)*fact(n-r)))

rows=int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        pascal_row=combo(i,j)
        print(pascal_row,end='')
    print('')
    
        
'''
lasith=[10,2000,300]
'''def isSorted(array):
    for i in range(1,len(array)):
        if array[i-1]>=array[i]:
            return False
    return True
print(isSorted(lasith))
'''
'''
def reverseList(array):
    right,left=len(array)-1,0
    while(left<right):
        array[left],array[right]=array[right],array[left]
        left+=1
        right-=1
    return(array)
print(reverseList(lasith))
'''

s='Hello World. I am Chitti. Speed 1 terahertz. Memory 1 zetabyte'
print (s[10])
print(s[3:21])
print(s[:10])
print(s[::-1])

s1='hello'
s2=s1
print(s1==s2)

s3=str(s1)
print(s1==s3)
s4=s1[:]
print(s1==s4)














