i = 0
while i < 3:
    print(i)
    i += 1
print()

while True:
    user_name = input("Enter user name or q to quit: ")
    if user_name == 'q':
        break
    if user_name == '':
        continue
    raw_count = input("Enter count: ")
    count = int(raw_count)
    print("Hello,", user_name * count)


