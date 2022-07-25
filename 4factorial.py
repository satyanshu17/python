num=int(input("Enter a number:"))
factorial=1
if num<0:
    print('factorial doees not exist')

elif num==0:
    print('the factorial of 0 is 1')

else:
    for i in range (1,num+1):
        factorial=factorial*i
    print('the factorial is',factorial)