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




