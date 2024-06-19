class Decorator(object):
    def __init__(self, func):
        self.function = func
    
    def __call__(self, *args):
        try:
            if any(isinstance(arg, str) for arg in args):
                raise TypeError("Cannot pass string as arguments")
            return self.function(*args)
        except Exception as obj:
            print(obj)

@Decorator
def add(*args):
    sum_ = 0
    for num in args:
        sum_ += num
    return sum_

print(add(10, 20, 30))
