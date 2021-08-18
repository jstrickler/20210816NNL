

class A:
    pass

class B(A):
    pass

class C(B):
    pass

c = C()

c_type = type(c)
parent = c_type.mro()[1]
grandparent = c_type.mro()[2]

print("mro:", c_type.mro())
print("parent:", parent)
print("grandparent:", grandparent)
