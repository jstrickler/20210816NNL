FILE_PATH = 'DATA/mary.txt'

with open(FILE_PATH) as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()  # "foo\n" to "foo"
        print(line)
print("-" * 60)

with open(FILE_PATH) as mary_in:
    contents = mary_in.read()  # read entire file
    print("RAW:")
    print(repr(contents))
    print("NORMAL:")
    print(contents)
print("-" * 60)

with open(FILE_PATH) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print("-" * 60)

with open(FILE_PATH) as mary_in:
    all_lines_without_nl = mary_in.read().splitlines()
    print(all_lines_without_nl)
