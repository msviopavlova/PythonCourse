number = input("Please enter a series of numbers, using any separators you like: ")
separators = ""  #empty string

for char in number: # extracting separators which isnt numeric from the input, then only the numbers are extracted from it and added together due to sum function down on line 11
    if not char.isnumeric():
        separators= separators+char

#print(separators)

values = "".join(char if char not in separators else "  "  for char in number).split()
print(sum([int(val) for val in values]))
