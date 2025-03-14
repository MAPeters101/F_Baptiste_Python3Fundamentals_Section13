def func(a=1):
    return a

print(func())
print(func(10))
print(func(a=10))

def func(a, b=10, c=20):
    return a, b, c

print(func(1))
print(func(1, 2))
print(func(1, 2, 3))
print('-'*80)

print(func(1, c=100))
print('-'*80)

def is_close(a, b, abs_tol=0.01):
    return abs(a - b) <= abs_tol

print(is_close(1.255, 1.256))
print(is_close(1255, 1256))
print(is_close(1255, 1256, abs_tol=5))
print('-'*80)

def parse(s, sep=',', strip=True):
    items = s.split(sep)
    if strip:
        return [item.strip() for item in items]
    else:
        return items

print(parse(' a,    b  ,  c  '))
print(parse(' a,    b  ,  c  ', strip=False))
print(parse('a:b. : c: d'))
print(parse('a:b. : c: d', sep=':'))
print(parse('a\n|b\n|c\n', sep='|'))
print(parse('a\n|b\n|c\n', sep='|', strip=False))
print('='*80)

print('a')
print('a', 'b', 'c')
print('d')
print('a', 'b', 'c', sep='---')
print(*'abc', sep=',', end='***')
print('next print line')





