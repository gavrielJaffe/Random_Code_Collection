from time import time

user1 = {
    'name':'dan',
    'validate_uesr':True
}

def authenticator(fun):
    def wrapper(*args , **kwargs):
        if (args[0]['validate_uesr']):
            return fun(*args , **kwargs)
          
    return wrapper


def timing(func):
    def wrapper_fun(*args, **kwars):
        time_before = time()
        func(*args,**kwars)
        time_after = time()
        print(f'Total time:{time_after-time_before}')
        return func(*args,**kwars)
    return wrapper_fun

# if the user has authentication,test time. 
@authenticator
@timing
def my_for(user):
    for i in range(10000):
        pass

my_for(user1)
