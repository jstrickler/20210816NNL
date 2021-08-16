import sys
print(sys.argv)  # argv is a list of words from cmd line

print(sys.argv[0])
print(sys.argv[1])
value = float(sys.argv[3])
print(value + 33)
print(len(sys.argv))
if len(sys.argv) == 1:
    print("Please enter a value on cmd line")
    sys.exit()

