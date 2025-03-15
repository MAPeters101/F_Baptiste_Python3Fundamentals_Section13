def func(a, b, *args, c):
    print(a)
    print(b)
    print(args)
    print(c)

func(10, 20, 30, 40, c=50)
#print(func(10, 20, 30, 40, 50))
print('-'*80)


def func(a, b, *, c):
    print(a)
    print(b)
    print(c)

func(10, 20, c=50)
#print(func(10, 20, 30))
func(c=1, b=2, a=3)
print('-'*80)





