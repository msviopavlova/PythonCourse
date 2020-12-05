parrot = "Norwegian Blue "

letter = input("Enyrt a character: ")
if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I dont't need that letter")
#string comparisons are case sensetive. a letter that was entered by user is being searched in parrot string.

# we are checking if something is in a sequence. we can check if something is NOT ina sequence by using NOT IN>

