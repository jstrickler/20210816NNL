a = "Alfred E. Neuman"
b = 32.93209302
c = "Fred Claus"

SEP = " "
END = "\n"
print(a)   # print(str(a) + END)
print(a, b)  # print(str(a) + SEP + str(b) + END)

print(a, b, sep="")
print(a, b, sep="/")
print(a, end=" ")  # print(str(a) + " ")
print(b)

print(b)
print(round(b, 2))
print("{:.2f}".format(b))
person = "Fred Flintstone"
city = "Bedrock"
print("{} lives in {}".format(person, city))
print(f"{b:.2f}")
print(f"{person} lives in {city}")

value = 12
print(f"{value:04d}")
print(f"{value:4d}")  # print("{:4d}".format(value))



