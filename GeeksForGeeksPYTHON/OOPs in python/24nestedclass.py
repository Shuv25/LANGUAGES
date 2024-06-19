class outer:
    def __init__(self):
        print("This is an outer class")
    def display(self):
        print("This is a display method")
    class inner:
        def __init__(self):
            print("This is an inner class")
        def show(self):
            print("This is a show method")

o=outer()
o.display()
i=o.inner()
i.show()