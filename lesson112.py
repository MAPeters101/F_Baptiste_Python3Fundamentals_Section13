
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


