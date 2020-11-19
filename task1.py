import time
import functools
from datetime import datetime
# from datetime import time

# task 1

# def hello_function(fn):
#     def wrapper():
#         if 9 <= datetime.now().hour < 21:
#             fn()
#         else:
#             print('Уже поздно')
#     return wrapper


# @hello_function
# def say_whee():
#     print('Whee!')
# say_whee()


# task 2

# def timer(func):
#     def tim(*args, **kwargs):
#         start_time = time.time()
#         res = func(*args, **kwargs)
#         print(('Время выполнения функции:', time.time() - start_time))
#         return res

#     return tim

# @timer
# def function(x, y):
#     return x + y

# function(123, 2121)


# task 3

# def repeat(num):
#     def wrapper(func):
#         @functools.wraps(func)
#         def wrapper_repeat(*args, **kwargs):
#             for i in range(num):
#                value = func(*args, **kwargs)
#             return value
#         return wrapper_repeat
#     return wrapper

# @repeat(num=4)
# def function(name):
#     print(f"{name}")

# function('Python')


# task 4
# Ne sdelal

# users = {'user1': 123, 'user2': 456, 'user3': 678}

# def login(username, password):
#     print(f'Wellcome, {username}')
#     return login
   

# @login
# def check():
#     try:    
#         print(users.values())
#     except Exception:
#         print('Password is invalid!')
#     try:
#         print(users.keys())
#     except Exception:
#         print('Username is not defind!')
#     return check
# check()
    

# task 5

def myDecorator(func):
    def wrapper(*args, **kwargs):
        print('Calling testFunc',(args, kwargs))
        print('argument a:', args[0])
        print('argument b:', args[1:2])
        print('argument args', args[2::])
        print('argument kwargs:', kwargs)
        print('Finished testFunc', args[3:])     
    return wrapper

    
@myDecorator
def testFunc(a, b=1, *args, **kwargs):
    return a + b
testFunc(2, 3, 4, 5, c=6, d=7)
print()
testFunc(2, c=5, d=6)
print()
testFunc(10)










