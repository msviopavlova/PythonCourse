if 0:   #python expects something after if so it tries to evaluate zero an boolean as well as name thing in the next example so it returns false as boolean/
    print("True")
else:
    print("False")

name = input("Please enter your name:  ")
#if name:
if name != "" : # HERE WE ARE COMARING NAME TO AN EMPTY STRING
    print("Hello, {}".format(name)) #if nothing is entered as a name it will say else, if name is entered it will say hello
else:
    print("Are you the man with no name? ")
