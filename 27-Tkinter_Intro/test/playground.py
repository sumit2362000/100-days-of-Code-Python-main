
'''Advanced Python Arguments'''
# functions often have arguments with default values. These values can be changed.

'''need * for function to accept any number of arguments, 'args' name can be changed'''
# def add(*args):
#     print(type(args)) # tuple type
#     result=0
#     for n in args:
#         result+=n
#     return result
# print(add(1,2,3,4,5,6,7,8,9))

'''unlimited key word arguments'''
def calculate(n, **kwargs):
    # print(type(kwargs))
    print(kwargs) # dictionary
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

# calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")
    
my_car = Car(make = "Nissan", model="GT_R")
# print(my_car.model)

def all_aboard(a, *args, **kw): 
    print(a, args, kw)
# all_aboard(4, 7, 3, 0, x=10, y=64) # 4 (7, 3, 0) {'x': 10, 'y': 64}