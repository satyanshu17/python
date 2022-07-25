#string formatting
#value of a is 6 and value of b is 6 then sum is 12

a,b=input('Enter the value of a & b is :').split(',')
c=int(a)+int(b)

#python 2

print('value of a is '+a+'and value of b is a '+b+' then sum is '+str(c) )

#python 3

print(f'value of a is {a} and value of b is {b} then sum is {c}')