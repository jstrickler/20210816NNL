items = list()  # instantiate the list class
# AKA creating an instance of list

# List items = new List(...);
items.append("duck")
items.append("duck")
items.append("goose")
print(items)

class Dog:
    def bark(self):
        print("woof! woof!")

d1 = Dog()
d2 = Dog()
d3 = Dog()
d1.bark()
d3.bark()

for d in d1, d2, d3:
    d.bark()

print(type(d1))


