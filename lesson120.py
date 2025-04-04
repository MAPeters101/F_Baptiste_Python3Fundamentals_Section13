print(2 + 2)
print(sum([1,2,3]) + max([0, -1, 1]))
a = 2 + 2
print(a)

print(lambda a, b: a + b)
print('-'*80)

f = lambda a, b: a+b

def add(a,b):
    return a+b

print(add)
print(f)
print()
print(f(10, 20))
print('-'*80)

f1 = lambda a, b, c: max(a,b,c)

def f2(a,b,c):
    return max(a,b,c)

print(f1(1,2,3), f2(1,2,3))
print('-'*80)


def identity(rows, cols):
    return [
        [1 if row == col else 0 for col in range(cols)]
        for row in range(rows)
    ]
print(identity(5,5))

f = lambda rows, cols: [
        [1 if row == col else 0 for col in range(cols)]
        for row in range(rows)
    ]
print(f(5,5))
print('='*80)

f = lambda a=0, b=2: a * b

print(f(10))
print(f('a'))
print(f('a', 10))
print('-'*80)

f = lambda a, *args: a * max(args)
print(f(10, 1,2,-1))

