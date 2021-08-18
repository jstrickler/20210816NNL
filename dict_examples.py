d1 = dict()  # empty dict
d2 = {'A': 5, 'M': 42, 'B': 16}
d3 = {}  # empty dict

d2['X'] = 5
d2['R'] = 42
print(d2)
d2['X'] = 18
print(d2)
print(d2['A'], d2['B'])

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}
print(airports['RDU'], airports['OAK'])

a2 = dict(airports)
data = [('IAD', 'Washington/Dulles'), ('PIT', 'Pittsburgh'),
        ('LAX', 'Los Angeles')]

for code, name in data:
    a2.setdefault(code, name)

print(a2)

for code in 'IAD', 'RDU', 'EWR', 'YOW', 'ZBA', 'LON', 'IHZ':
    print(code, airports.get(code, 'NOT FOUND'))

more_airports = {'JAX': 'Jacksonville', 'MIA': 'Miami',
                 'ELM': 'Elmira/Corning', 'RDU': 'Durham/Raleigh'}

airports.update(more_airports)
print(airports)

print(len(airports))

del airports['OAK']
print(airports)
# for  key,   value in DICT.items()
for code, name in airports.items():
    print(code, name)

print(airports.keys())
print(airports.values())




