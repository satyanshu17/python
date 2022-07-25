#list--. list command--> range function
num=list(range(1,11))
print(num)
#print(type(num))
even=[]
new=[]
for i in num:
    new.append(-i)
    if i%2==0:
        even.append(i)
print(even)
print(new)