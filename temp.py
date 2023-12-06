
n1 = [x for x in range(10) if x % 2 == 0] # 0,2,4,6,8
n2 = [x for x in range(10) if x % 2 != 0]

print(f'{n1} {n2}')
zipped = list(zip(n1,n2))
print('zipped',zipped)

zipped2 = zipped[::-1]
zipped2.extend(n2[::-1])
print('zipped2', zipped2)

n1[-5:-5] = [999] # 999,0,2,4,6,8
n1[1:4] = ["a","b","c"] # 999,a,b,c,6,8
print('n1', n1) # 999,a,b,c,6,8


ls2 = isinstance(n1,int)
print('ls2', ls2)

lst = sorted(n1, key=lambda x :(isinstance(x, int), x), reverse=True)
print('lst', lst)







