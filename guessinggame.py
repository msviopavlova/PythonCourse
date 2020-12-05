import random

highest = 10

answer = random.randint(1, highest) #the dot tells that randint is inside random(and produces a random number within the vaklues specified)
print(answer) #TODO: remove after testing
print("Please guess a number between 1 and {} ".format(highest))
guess = int(input())

if guess == answer:
    print("You got it first time")
else:
    if guess < answer:
        print("Please  guess higher")
    else:
        print("Please guess lower")
    guess = int(input())    # single = sign is used when binding a variable to a value.
    if guess ==answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")

