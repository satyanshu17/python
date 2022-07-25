#function returning function

def outer(msg):
    def inner():
        print(f'Hello i am Function  {msg}')
    return inner()



var=outer('Good Bye')
