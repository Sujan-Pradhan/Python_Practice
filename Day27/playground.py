def add(*args):
    print(args[0])
    sum = 0
    # print(type(args))
    for numbers in args:
        # print(type(numbers))
        sum += numbers
    # print(sum)
    return sum

# add(2,3,4,1)
# print(add(2,3,4,1))

def calculate(n,**kwargs):
    print(type(kwargs))
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n*=kwargs["multiply"]
    n/=kwargs["divide"]
    print(n)



calculate(2,add = 3, multiply = 4, divide =2)

class Car:
    def __init__(self,**kwargs):
        self.make = kwargs["make"]
        # self.model = kwargs["model"]
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")

my_car = Car(make = "Ferrari")
print(my_car.model)
