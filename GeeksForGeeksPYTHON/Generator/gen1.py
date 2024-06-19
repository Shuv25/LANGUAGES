def romote_control():
    yield 'setmax'
    yield 'zee'

r=romote_control()
itr=iter(r)
print(next(itr))
print(next(itr))