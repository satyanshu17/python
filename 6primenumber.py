#prime nuber between 1 to 100

for num in range(2,101):
    count=0
    for i in range(2,(num//2+1)):
        if(num%i==0):
            count=count+1
            break
    if (count==0 and num!=1):
        print(num)
     
     
