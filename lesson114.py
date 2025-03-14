
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





