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

def is_close(a, b, abs_tol=0.01):
    return abs(a - b) <= abs_tol

print(is_close(1.255, 1.256))
print(is_close(1255, 1256))
print(is_close(1255, 1256, abs_tol=5))
print('-'*80)

def parse(s, sep=',', strip=True):
    items = s.split(sep)
    if strip:
        return [item.strip() for item in items]
    else:
        return items

print(parse(' a,    b  ,  c  '))
print(parse(' a,    b  ,  c  ', strip=False))
print(parse('a:b. : c: d'))
print(parse('a:b. : c: d', sep=':'))
print(parse('a\n|b\n|c\n', sep='|'))
print(parse('a\n|b\n|c\n', sep='|', strip=False))
print('='*80)

print('a')
print('a', 'b', 'c')
print('d')
print('a', 'b', 'c', sep='---')
print(*'abc', sep=',', end='***')
print('next print line')
print('-'*80)


data = [
    [10, 20, 30],
    [100, 200, 300],
    [1000, 2000, 3000]
]

def process_data(data, item_sep=',', line_sep='\n'):
    output = ''

    for row in data:
        for element in row:
            output = output + str(element) + item_sep
        output = output + line_sep

    return output

print(process_data(data))
print('-'*80)

print(process_data(data, item_sep='=='))
print('-'*80)

print(process_data(data, item_sep='==', line_sep='\n\n'))
print('-'*80)

print(process_data(data))
print('done')
print('-'*80)


print('-'.join(['a', 'b', 'c']))
print('-'.join(*['abc']))
print(','.join(['a', 'b', 'c']))
print('-'*80)


data = [
    [10, 20, 30],
    [100, 200, 300],
    [1000, 2000, 3000]
]

def process_data(data, item_sep=',', line_sep='\n'):
    output = ''

    for row in data:
        row_str = item_sep.join([str(el) for el in row])
        output = output + row_str + line_sep

    return output

print(process_data(data))
print('-'*80)
print(process_data(data, line_sep='=='))
print('-'*80)

data = [
    [10, 20, 30],
    [100, 200, 300],
    [1000, 2000, 3000]
]

def process_data(data, item_sep=',', line_sep='\n'):
    output = ''

    for row in data:
        gen = (str(el) for el in row)
        row_str = item_sep.join(gen)
        output = output + row_str + line_sep

    return output

print(process_data(data))
print('-'*80)

data = [
    [10, 20, 30],
    [100, 200, 300],
    [1000, 2000, 3000]
]

def process_data(data, item_sep=',', line_sep='\n'):
    output = ''

    for row in data:
        row_str = item_sep.join(str(el) for el in row)
        output = output + row_str + line_sep

    return output

print(process_data(data))
print('-'*80)

data = [
    [10, 20, 30],
    [100, 200, 300],
    [1000, 2000, 3000]
]

def process_data(data, item_sep=',', line_sep='\n'):
    row_strings = [
        item_sep.join(str(el) for el in row)
        for row in data
    ]
    return row_strings

print(process_data(data))
print('='*80)


data = [
    [10, 20, 30],
    [100, 200, 300],
    [1000, 2000, 3000]
]

def process_data(data, item_sep=',', line_sep='\n'):
    row_strings = [
        item_sep.join(str(el) for el in row)
        for row in data
    ]
    return line_sep.join(row_strings)

print(process_data(data))
print('-'*80)


