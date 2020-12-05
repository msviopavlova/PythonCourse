shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
    if item == "spam":
        break
# we wont get a reminder as the executinon wil stop as it reaches spam.
    print("Buy " + item)

# imagine we are searching through a list containing thousands of items
# if we find the item we are looking for, we will stop looking.