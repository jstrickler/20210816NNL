list1 = list()  # empty list
# [1, 2, 3]
list2 = [1, 5, 19, 2, 37]
words = "blark kringel huffnel".split()
print(list1, list2, words)
list3 = []  # empty

cities = ['McKeesport', "Albany", "Colonie",
          "Homestead"]
print(cities, len(cities))
cities.append("Saratoga Springs")
cities.append("Omaha")
print(cities)
cities.insert(0, "Durham")
cities.insert(4, "Rochester")
print(cities)
more_cities = ["West Mifflin", "Sewickley", "Monroeville"]
cities.extend(more_cities)
print(cities)

# make a list bigger
# LIST.append(obj)  LIST.insert(pos, obj) LIST.extend(ITERABLE)

del cities[3]    #   del LIST[pos]  del ANY_VARIABLE
print(cities)

c = cities.pop()  # remove last element
print(c)
print(cities)
c = cities.pop(3) # remove 4th element
print(c)
print(cities)
cities.remove('Omaha')
print(cities)

# make a list smaller
# del LIST[pos]   LIST.pop()  LIST.pop(pos)  LIST.remove(value)

cities[0]  = "Raleigh"
print(cities)
# cities[20] = "Springfield"  only assign to existing element
print(cities[0], cities[5])
print(cities[-1])   #  cities[len(cities) - 1]
print(cities[-7])
cities.append("Troy")
cities.append("Schenectady")
cities.append("Boston")
cities.append("Ohiopyle")
print(cities)

print(cities[0:4])
print(cities[4:7])

# OBJ[START:STOP]  OBJ[:STOP]  OBJ[START:] OBJ[START:STOP:STEP]
s = "Python is the best"
print(s[:6])
print(s[-4:])
print(s[4:9])
print()

# for VAR in ITERABLE
#    VAR = next element of ITERABLE
for city in cities:
    print(city)
print()

# iterables: str bytes list tuple dict set <generators>

s = "abc"
for char in s:
    print(char.upper())
print()



