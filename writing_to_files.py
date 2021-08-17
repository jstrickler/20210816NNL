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

with open('geeks.txt', 'w') as geeks_out:
    for person in people:
        data = '\t'.join(person)
        geeks_out.write(data + '\n')

with open('DATA/words.txt') as words_in:
    with open('zwords.txt', 'w') as zwords_out:
        for raw_line in words_in:
            if 'z' in raw_line:
                zwords_out.write(raw_line)

