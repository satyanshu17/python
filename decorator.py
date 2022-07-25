#decorator---> enhance the functionality of other function
#working like a decorator
#@ original decorator

def decorator(any_function):
    def wrapper():
        print('i am calling main function')

        any_function()
    return wrapper

#i am calling main function
@decorator
def func1():
    print ('This is function 1')

#i am calling main function
@decorator
def func2():
    print('This is function 2')

#var=decorator(func1)
#var()
#var1=decorator(func2)
#var1()
func1()
func2()