#math
import math

x=5.7
print(math.ceil(x))
print(math.floor(x))
print(math.trunc(x))#will remove all the decimal parts

y=3
print(math.exp(y))
print(math.log(y))
print(math.sin(y))
print(math.cos(y))
print(math.tan(y))
print(math.pi)
print(math.e)
print(math.factorial(5))
print('-'*30)

#random
import random

print(random.random())
print(random.randint(3,8))
print(random.choice([3,4,5,6,7,8]))
print(random.sample([3,4,5,6,7,8],3))
print(random.uniform(3.0,7.0))
print('-'*30)

#datetime
import datetime

print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%d:%m:%y %H:%M:%S"))#can change the format of printing
print(datetime.datetime.now().strftime("%m:%d:%y %H:%M:%S"))#can change the format of printing
mob=datetime.datetime(2019,7,12,3,40,30)
print(datetime.datetime.now()-mob)
print('-'*30)

#collections
from collections import Counter, defaultdict
l=[3,3,4,4,4,5,6,7,7,6,6,6]
print(Counter(l))

d=defaultdict(int)
d['a']+=3
print(d)

d=defaultdict()
d['one']=1
d['two']=2
print(d)
print('-'*30)

#string

import string

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)#all the spcial characters

