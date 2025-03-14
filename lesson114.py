
def my_func(*args):
    print(type(args))
    print(args)

my_func()
my_func(1)
my_func(1,2,3,4, [1,2], 'abc')
print('-'*80)

def my_func(a, b, *args):
    print(a)
    print(b)
    print(args)

my_func(1,2)
my_func(1,2,3,4,5)
print('='*80)


def my_func(a, b, *args, c):
    print(a)
    print(b)
    print(args)
    print(c)

#my_func(1,2)
#my_func(1,2,3,4,5)
my_func(1,2,3,4,c=5)
print('-'*80)


# def my_func(a, b, *args,*extrasc):
#     print(a)
#     print(b)
#     print(args)
#     print(c)
#
# #my_func(1,2)
# #my_func(1,2,3,4,5)
# my_func(1,2,3,4,5)
# print('-'*80)

print(sum({1,2,3}))

def averages(*values):
    return sum(values) / len(values)

print(averages(1))
print(averages(1,2,3))
print(averages(1,3,5,7,9,11))
print(averages(0))
print('+'*80)

def averages(*values):
    try:
        return sum(values) / len(values)
    except ZeroDivisionError:
        return 0

print(averages(1))
print(averages(1,2,3))
print(averages(1,3,5,7,9,11))
print(averages(0))
print('-'*80)

def averages(*values):
    if len(values) == 0:
        return 0
    return sum(values) / len(values)

print(averages(1))
print(averages(1,2,3))
print(averages(1,3,5,7,9,11))
print(averages(0))
print('.'*80)

def product(*values):
    prod = 1
    for value in values:
        prod *= value
    return prod

print(product(1,2,3))
print(product(1,2,3,4))
print(product())
