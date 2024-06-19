with open('one.txt','w+') as f:
    f.write("Hello Everyone\nHow are you\n guys")
    f.seek(0)
    content=f.read()
    
print(content)

with open('one.txt','w+') as f:
    f.write("Hello Everyone\nHow are you\n guys")
    f.seek(0)
    newcontent=f.readline()
    
print(newcontent)

with open('one.txt','w+') as f:
    f.write("Hello Everyone\nHow are you\n guys")
    f.seek(0)
    lastcontent=f.readlines()
    
print(lastcontent)