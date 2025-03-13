
def say_hello():
    return 'hello!'


print(globals())
a = 100
print(globals())
print(type(say_hello))
result = say_hello()
print(result)
f = say_hello
print(globals())
print('-'*80)

l1 = [1,2,3]
print(globals())
l2 = l1
print(globals())
print(l1 is l2)
print(f is say_hello())
print(say_hello())
print(f())
print(say_hello.__name__)
print(f.__name__)
print('='*80)


def add(a,b,c):
    print(f'a={a}')
    print(f'b={b}')
    print(f'c={c}')
    return a+b+c

result = add(1,2,3)
print(result)

def add(a,b,c):
    print('initial namespace:', locals())
    sum_ = a+b+c
    print('after sum_ namespace:', locals())
    return a+b+c

result = add(1,2,3)
print(result)

result = add(10,20,30)
print(result)
print('-'*80)

def find_max(a, b, c):
    max_ = a
    if b>max_:
        max_=b
    if c>max_:
        max_=c
    return max_

print(find_max(10, 20, 30))
print('-'*80)




