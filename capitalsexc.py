quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
# # my solution
#
# for char in quote:
#     if not char.islower():
#         print(char)

# solution from the udemy
for char in quote:
    if char.isupper():
        print(char)
