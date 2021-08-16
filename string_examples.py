s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''''
s5 = r"spam\n"   # Windows paths, REs maybe LaTex

print(s1)
print(len(s1))
print("It's......Monty Python's Flying Circus")
print('Guido van Rossum is the "BDFL Emeritus" of Python')

print("""Guido van Rossum's the "BDFL etc" of Python""")

query = """
select *
from animals
where animal = "wombat"
"""

print(query)   # print(str(query))
print(repr(query))  # raw (code) view of string
print()

actor = "Chris Hemsworth"
print(type(actor), len(actor))

a = actor.upper()
print(a)
print(actor.upper())
print(actor.count('h'))
print(actor.count('H'))
print(actor.lower().count('h'))
print(actor.startswith('Chris'))
print(actor.startswith('Liam'))
print(actor.find('Chris'))
print(actor.find('worth'))
print(actor.find('Liam'))
print(actor.replace(' ', ''))
print(actor.replace(' ', '').isalpha())
print(actor.replace('Chris', 'Liam'))
s = "fee fi fo fum"
words = s.split()
print(words)

s = "one/two/three/four"
words = s.split('/')
print(words)
s2 = ",".join(words)
print(s2)

s = "==a==b==c=="
print(s.split('=='))

import re
s = "foo//bar;;blah"
words = re.split('(?://|;;)', s)
print(words)

s = "     All my exes live in Texas      "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

n = "0000000535"
print(n.lstrip("0"))

x = ".....wombats,,,,,"
print(x.strip(".,"))
