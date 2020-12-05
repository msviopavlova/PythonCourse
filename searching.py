shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "rice"
found_at = None

# None i a constant to show that something doesnt have a value (Null in C or Java)
#we are attaching a variable to something that does not have a value

# we are gonna loop over the index positions of the list instead of over the items.

#это комментарий. for index in range(6):
###for index in range(len(shopping_list)):
   ### if shopping_list[index] == item_to_find:  # len is short for length and shows how many items are in a sequence
      ###  found_at = index
# вот тот же самый код только написаный короче  и другими словами
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
if found_at is not None:
    print("Item found at position {}".format(found_at)) # count starts from 0
else:
    print("{} not found".format(found_at))
# этот код ищет item_to_find(строка 3) и если там слово, которого нет в списке
# то он выдаст ответ None (found_at)

