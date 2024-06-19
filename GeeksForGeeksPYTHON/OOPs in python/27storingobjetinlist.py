class movies:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)

l=[]
while True:
    x=input("Enter the movie name:")
    m=movies(x)
    l.append(m)
    a=input("Do u want to continue:y/n")
    if(a=='n'):
        break

for i in l:
    i.show()