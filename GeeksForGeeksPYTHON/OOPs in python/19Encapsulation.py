class details:
    def __init__(self,name,salary):
        self.__name=name#to make a variable private
        self.__salary=salary
    def show(self):
        print(self.__name)
        print(self.__salary)


d=details("Shuv",70000000)
#print(d.__name)#it will be not accesible now
print(d._details__name)#but we can ue name wrangling to use the private variable, for that we need to use class name with single unserscore then two undersore with variable name
d.show()