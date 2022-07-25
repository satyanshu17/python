#lamda function

#lambda variable : operation

add=lambda a,b:a+b
print(add(2,4))

square=lambda a:a**2
print(square(9))

#map function

#map (function,input)
num=[1,2,3,4,5]
def square(a):
    return a**2

print(map(square,num))
print(list (map(square,num)))

print(list (map(lambda a:a**2,num)))

