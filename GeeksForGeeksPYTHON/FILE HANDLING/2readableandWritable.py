import os
with open('one.txt','r') as f:
    print(f.readable())
    print(f.writable())
    
with open('one.txt','w') as f:
    print(f.readable())
    print(f.writable())

if os.path.isfile('two.txt'):
    print("File is exist")
else:
    print("File is not exist")