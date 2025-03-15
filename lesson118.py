def func(a, b, *args, c):
    print(a)
    print(b)
    print(args)
    print(c)

print(func(10, 20, 30, 40, c=50))
print(func(10, 20, 30, 40, 50))

