
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

for i, fruit in enumerate(fruits):
    print(i, fruit)
print()

print(list(enumerate(fruits)), '\n')

#  * +
print("-" * 10)
print([False] * 5)
x = "a b c".split()
y = "d e f".split()
print(x + y)

e = enumerate(fruits)
print(next(e))  # next() says "give me next element"
print(next(e))
notes = ['do', 're', 'mi']
notes_iterator = iter(notes)  # get iterator from container
print(next(notes_iterator))
print(next(notes_iterator))
x = 199

del notes[1]
print(notes)
for note in notes:
    print(note, note in notes)

# in:   value in LIST
#       key in DICT
#      substr in STRING
#      member (element) in SET
print("foo" in "football")
print("apple" in fruits)
print("bar" in "football")
print("carrot" in fruits)

