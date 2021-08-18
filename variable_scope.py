
x = 100  # global variable visible to end of current file

def spam(toast):
    print("In spam(): x is", x)
    animal = "wombat"  # local variable visible to end of function


spam("whole-wheat")

print("in main: x is", x)
# print("in main: animal is", animal)

def mutt():
    color = "blue"
    print(color.upper())  # color is local here

    def jeff():
        print("color is", color)  # color is nonlocal here

    return jeff

f = mutt()
f()  # call (invoke) the function object
mutt()  # ignore return value

class Foo():
    def bar(self):
        print("bar bar bar")

def ham():
    f = Foo()
    return f

x = ham()
x.bar()

def blurg():
    return "blah"

print(blurg)
print(blurg())

def flugg():
    return

print(flugg, flugg())

mutt()()   #  x = mutt(); x()






