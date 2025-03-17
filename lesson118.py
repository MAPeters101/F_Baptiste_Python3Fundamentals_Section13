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
print('-'*80)


def process_data(data, item_sep=',', line_sep='\n'):
    row_strings = [item_sep.join([str(element) for element in row])
                   for row in data]
    return line_sep.join(row_strings)

data = [
    [10, 20, 30],
    [100, 200, 300],
    [1000, 2000, 3000]
]

print(process_data(data, ':', '\n\n'))
print(process_data(data, item_sep=':', line_sep='\n\n'))
print('-'*80)


def process_data(data, *, item_sep=',', line_sep='\n'):
    row_strings = [item_sep.join([str(element) for element in row])
                   for row in data]
    return line_sep.join(row_strings)

data = [
    [10, 20, 30],
    [100, 200, 300],
    [1000, 2000, 3000]
]

#print(process_data(data, ':', '\n\n'))
print(process_data(data, item_sep=':', line_sep='\n\n'))
print('-'*80)

def coords_to_json(longitude, latitude):
    return f'{{"longitude": {longitude}, "latitude": {latitude}}}'

print(coords_to_json(10, 20))
print(coords_to_json(longitude=10, latitude=20))
print('-'*80)

def coords_to_json(*, longitude, latitude):
    return f'{{"longitude": {longitude}, "latitude": {latitude}}}'

#print(coords_to_json(10, 20))
print(coords_to_json(longitude=10, latitude=20))
print('-'*80)

def func(a, b, *args, c, d, **kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kwargs)

func(10, 20, 30, 40, 50, c=1, d=2, x=100, y=100)
func(c=1, d=2, x=100, y=200, a=10, b=20)
#func(20, 30, c=1, d=2, x=100, y=200, a=10, b=20)
#func(a=10, b=20, 20, 30, c=1, d=2, x=100, y=200)
print('-'*80)

def func(**kwargs):
    return kwargs['a'] + kwargs['b']

print(func(a=10, b=20, c=30))

def func(*, a, b):
    return a + b

print(func(a=10, b=20))

def func(**kwargs):
    # expecting data1, data2, arg1, arg2, arg3, arg4
    pass

def func(data1, data2, arg1, arg2, arg3, arg4):
    # expecting data1, data2, arg1, arg2, arg3, arg4
    pass

def to_json(arg1, *, kw1, **extras):
    formatted_extras = ', '.join([f'"{key}": {value}' for key, value in extras.items()])
    result = f'{{"arg1": {arg1}, "kw1": {kw1}, "extras": {{{formatted_extras}}}}}'
    return result

print(to_json(10, kw1=20, a=1, b=2, c=3))
# {"arg1": 10, "kw1": 20,"extras": {"a": 1, "b": 2, "c": 3}}



