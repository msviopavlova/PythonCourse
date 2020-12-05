shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        continue # continue causes all the remaining code in the block to be skipped (print wont execute! it goes straigh back up to the for line 7)
# i may never use continue and in many languages it doesnt exist . there arw possible uses of it.
    print("Buy " + item)