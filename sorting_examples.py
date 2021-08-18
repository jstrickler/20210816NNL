fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date"]

f1 = sorted(fruits)
print("f1:", f1, '\n')

f2 = sorted(fruits, key=str.lower)
print("f2:", f2, '\n')

def ignore_case(s):
    compare_value = s.lower()
    print(f"comparing {s} as {compare_value}")
    return compare_value

f3 = sorted(fruits, key=ignore_case)
print("f3:", f3, '\n')

f4 = sorted(fruits, key=len)
print("f4:", f4, '\n')

def custom_sort(fruit):
    return len(fruit), fruit.lower()

f5 = sorted(fruits, key=custom_sort)
print("f5:", f5, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

def by_dob(person):
    return person[3]  # or person[-1]

for person in sorted(people, key=by_dob, reverse=True):
    print(person)
print()

for person in sorted(people, key=lambda p: p[3]):
    print(person)
print()

# lambda p, ...: EXPR

# def NAME(p, ...):
#     return EXPR

def make_upper(s):
    return s.upper()

def make_lower(s):
    return s.lower()

def show_text(text, func):
    print(func(text))

show_text("Spam", make_upper)
show_text("Spam", make_lower)



