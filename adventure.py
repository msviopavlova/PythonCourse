available_exits = ["north", "south", "east", "west"]

chosen_exit ="" # this means its an empty string  and nothing is entered
while chosen_exit not in available_exits: # coz am empty string is not in a list , the condotion evaluates to True
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":  #casefold() function is to convert the entry into lowercase
        print("Game over")
        break


print("aren't you glad you got out of there")


# while loops are good for when you dont know in advance how many times u will need to loop

#A FOR loop will repeat for each item in a pre determined sequence whereas with a while loop you dont need to know how many times th eloop will excute.

# a while loop can be used to keep reading until there is no more data left
# we ;; use it soon in input and putpit in python
