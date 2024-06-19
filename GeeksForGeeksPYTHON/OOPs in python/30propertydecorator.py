class details:
    def __init__(self,fnam,lname):
        self.fname=fnam
        self.lname=lname
    
    @property#it is builtin decorator
    def mail(self):
        return f"{self.fname}{self.lname}@fmail.com"
    
d=details("Shuv","Sutradhar")
print(d.fname)
print(d.lname)
print(d.mail)
d.fname="sourav"#when we chnge the value using object it will automatically change the ther property due to proprty decerator
print(d.mail)
d.lname="roy"
print(d.mail)