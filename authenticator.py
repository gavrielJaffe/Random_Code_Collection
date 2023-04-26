from time import time
# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:

user1 = {
    'name':'dan',
    'validate_uesr':False
}

def authenticator(fun):
    def wrapper(*args , **kwargs):
        if (args[0]['validate_uesr']):
            return fun(*args , **kwargs)
          
    return wrapper

@authenticator
def chack_authe(user):
    print("validation of the user is True")

chack_authe(user1)

# *******************************************************************************************8
from time import time

def timing(func):
    def wrapper_fun(*args, **kwars):
        time_before = time()
        func(*args,**kwars)
        time_after = time()
        print(f'Total time:{time_after-time_before}')
        return func(*args,**kwars)
    return wrapper_fun



@timing
def my_for(i):
    for i in range(10000):
        pass

my_for(1)