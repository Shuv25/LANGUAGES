def addbehav(func):
    def wrapper():
        print("Adding something before function call")
        func()
        print("Adding something after function call")
    return wrapper

@addbehav
def show():
    print("Hello")

show()