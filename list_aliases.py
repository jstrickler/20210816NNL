from copy import deepcopy
x = ['do', 're', 'mi']
y = x   # alias 'y' to 'x'  (alias, not copy)
print(x)
print(y)
z = list(x)  # initialize NEW list from x (shallow copy)
m = deepcopy(x)   # initalize m from x RECURSIVELY
print(z)
x.append('fa')
print(x, y, z)
a = "apple"
b = "apple"
print(a is b)