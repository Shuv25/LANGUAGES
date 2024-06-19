class human:
    def __init__(self):
        print("Human class constructor is called")
        self.name = input("Enter your name:")


class employee(human):
    def __init__(self):
        super().__init__()
        print("Employee class constructor is called")
        self.designation = input("Enter your designation:")


class manager(employee):
    def __init__(self):
        super().__init__()
        print("Manager constructor is called")
        self.salary = int(input("Enter salary:"))

    def display(self):
        print("Name:", self.name)
        print("Designation:", self.designation)
        print("Salary:", self.salary)


m1 = manager()
m1.display()
