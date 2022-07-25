# for loop
'''
for i range(1,11):
    print(i)
'''

def sum2(n):
    sum1=0
    for i in range(1,n+1):
        if i%2==0:
            print(i)
            sum1=sum1+i
    return sum1
print(sum2(10))
