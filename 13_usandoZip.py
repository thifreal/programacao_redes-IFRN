chaves = ['a','b','c','d']
valores = [1,2,3,4]
D1 = dict(zip(chaves, valores))
print(D1)
D2 = {k: v for (k, v) in zip(chaves, valores)}
print(D2)
