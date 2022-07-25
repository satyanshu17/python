#@ original decorator

def decorator(any_function):
    def wrapper(*args,**kwarg):
        print('i am calling main function')

        return any_function(*args,**kwarg)
    return wrapper

#i am calling main function
@decorator
def func1():
    print ('This is function 1')

@decorator
def add(a,b):
    return a+b
print(add(2,3))