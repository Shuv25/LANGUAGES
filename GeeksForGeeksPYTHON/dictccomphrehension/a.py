l=[3,4,5,6,7,8,9]
dicty={i:i*i for i in l}
print(dicty)
dicty={i:i*i for i in l if i%2==0}
print(dicty)
dicty={i:i*i for i in l if i%2==0 if i%3==0}
print(dicty)
dicty={i:i*i if i%2==0 else i*i*i for i in l}
print(dicty)

