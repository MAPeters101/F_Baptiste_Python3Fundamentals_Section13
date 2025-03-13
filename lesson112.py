
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


