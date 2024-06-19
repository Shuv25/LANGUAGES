l=['shuv','sourav','roy']
ll=[3,4,5]
print(list(zip(l,ll)))
print('-'*30)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print([list(i) for i in zip(matrix)])
print([list(i) for i in zip(*matrix)])

listone=[3,4,5]
listtwo=[6,7,8]
print([i*j for i,j in zip(listone,listtwo)])
print(sum([i*j for i,j in zip(listone,listtwo)]))