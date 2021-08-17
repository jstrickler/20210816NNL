
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

print(len(fruits), min(fruits), max(fruits))
print(sorted(fruits))
print()

r = reversed(fruits)
print(r, type(r))
for fruit in r:
    print(fruit)
print()