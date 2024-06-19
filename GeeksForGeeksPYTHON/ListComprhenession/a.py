#type a
l=[3,4,5,6,7,8,9]
sq=[i*i for i in l]
print(sq)

#type b if there is any if condition
evensq=[i*i for i in l if i%2==0]
print(evensq)

#type c if there any nested if

divby2nd3=[i*i for i in l if i%2==0 if i%3==0]
print(divby2nd3)

#type d if there if and else condition

ifelse=[i*i if i%2==0 else i*i*i for i in l]
print(ifelse)

#type e if there is any nested for loop
nestedfor=[i*j for i in range(5,7) for j in range(3,6)]
print(nestedfor)

