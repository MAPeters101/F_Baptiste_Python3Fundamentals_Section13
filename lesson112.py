
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

from datetime import datetime
def log(message):
    curr_time = datetime.utcnow().isoformat()
    print(f'{curr_time} - [{message}]')
log('log 1')
result = log('log 1')
print(type(result))
print(result)
print('-'*80)


data = [1,2,3,4,5,6]
for element in data:
    if element < 0:
        break
else:
    print('processing all positive elements')
print('-'*80)

def is_all_positive(data):
    for element in data:
        if element < 0:
            return False
    return True
print(is_all_positive([1,2,3,4]))
print(is_all_positive([10,3,-4,100]))
print(is_all_positive(range(1,10)))
print(is_all_positive(range(10,-20, -2)))
d = {'a':1, 'b':2, 'c':-10}
print(is_all_positive(d.values()))
print('-'*80)



def gen_matrix(m, n, default_value):
    return [[default_value for i in range(n)] for j in range(m)]

print(gen_matrix(2, 2, 1))
print(gen_matrix(4, 8, 1))

def gen_matrix(rows, cols, default_value):
    return [[default_value for i in range(cols)] for j in range(rows)]

print(gen_matrix(2, 2, 1))
print(gen_matrix(4, 8, 1))
print(gen_matrix(rows=4, cols=8, default_value=1))
print(gen_matrix(cols=8, rows=4, default_value=1))
print('-'*80)
#print(gen_matrix(5, rows=4, default_value=1))
#print(gen_matrix(5, cols=4, 1))
print(gen_matrix(5, cols=4, default_value=1))







