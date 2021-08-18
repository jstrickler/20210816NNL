
values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)

def spam(a, b):
    print(f"a is {a} b is {b}")

spam(1, 2)
spam('a', 'b')
spam('foo', 'bar')

x = [5, 10]
spam(x[0], x[1])
spam(*x)
spam(5, 10)
print()

data = [('a', 5), ('m', 42), ('x', 14)]
for m in data:
    spam(*m)




