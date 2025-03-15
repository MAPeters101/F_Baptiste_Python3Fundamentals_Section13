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

def func(a, b=2, c=3, *, d=10, e, f=30):
    print(a, b, c, d, e, f)

func(1, e=20)
func(e=20, a=1)
func(1, c=3.5, d=100, e=200)

