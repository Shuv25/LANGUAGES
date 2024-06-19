age = int(input("Enter the age:"))
with open('one.txt', 'w') as f:
    f.write(str(age))

with open('one.txt', 'r') as f:
    content = f.read()
    print(content)
print(f.name)
print(f.mode)
print(f.encoding)
print(f.buffer)
print(f.closed)
