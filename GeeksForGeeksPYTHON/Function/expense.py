def get_expense(l):
    total=0
    for i in l:
        total=total+i
    return total

l=[400,500,600]
ll=[300,500,600]

print(get_expense(ll))