class cart:
    def __init__(self,phone,laptop,watch):
        self.phone=phone
        self.laptop=laptop
        self.watch=watch
    def __len__(self):
        print("The length of cart is:")
        return len(self.phone)+len(self.laptop)+len(self.watch)

c=cart(['iphone','samsung','realme'],['macbook','asus','dell','hp'],['rolex','titen'])
print(len(c))