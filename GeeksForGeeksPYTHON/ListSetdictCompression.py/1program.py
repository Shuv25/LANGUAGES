l=[1,2,3,4,5,6,7,8,9]
even=[]
even=[i for i in l if i%2==0]
print(even)

sqrt_no=[i*i for i in l]
print(sqrt_no)

s=[1,2,3,4,5,6,7,8,9]

seven={i for i in s if i%2==0}
print(seven)

cities=['mumbai','moscow','tokyo']
country=['india','russia','japan']

z=zip(cities,country)
d={city:country for city, country in z}
print(d)