numbers = [1, 45, 31, 16, 60]
#square brackets are a sequemce type

for number in numbers:
    if number % 8 == 0:
        #reject the list
        print("The numbers are unacceptable")
        break
        # when our loop finds a value thats unacceptable, out code
        # breaks out of the loop
        #that means the loop will only terminate normally
        #if all the values are acceptable
        # we want to run some code when the loop terminates normally.
else: # has to be with the level ofthe FOE
    print("All those numbers are fine")
    #its only the indentation level that ties the else to the for
    