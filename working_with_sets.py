letters = ['a', 'b', 'm', 'm', 'a', 'x', 'y', 'b']
s1 = set(letters)
print(s1, '\n')
s2 = {'a', 'm', 'x', 'a', 'a', 'a', 'a', 'c', 'b', 'a'}
print(s2, '\n')
s2.add('m')
s2.add('r')
s2.add('m')
print(s2, '\n')

d1 = ['red', 'blue', 'mauve', 'puce', 'maroon', 'pink', 'black']
d2 = ['blue', 'brown', 'puce', 'black', 'orange', 'red', 'red']

s1 = set(d1)
s2 = set(d2)
print(s1)
print(s2, '\n')

print("Both (intersection):", s1 & s2)
print("Just one (Xor):", s1 ^ s2)
print("Either (union):", s1 | s2)
print("Just s1:", s1 - s2)
print("Just s2:", s2 - s1)
