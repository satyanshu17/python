n=[1,2,3,4,5,6,7,8,9]

def Square(a):
    return a%2==0

print(filter(Square,n))

print(list(filter(lambda a:a%2==0,n)))

print(list(filter(lambda a:'even' if a%2==0 else 'odd', n)))