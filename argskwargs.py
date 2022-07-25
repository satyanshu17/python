#args
#kwargs

#  * operator
# ** operator

def add(a,b):
    return a+b

print(add(2,3))

def add(*args):
    return args

print(add(1,2,3,4,5))


def add(*args):
    print(args)
    total=0
    for i in args:
        total=total+i
    return total

n=int(input('enter your range'))
num=list(range(1,n+1))
print(add(*num))