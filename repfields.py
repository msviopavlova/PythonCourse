age = 24
print("My age is {0} years".format(age))
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "January", "March", "May", "July", "August", "October", "December"))

#номер в кривых скобках будет заменем на то что идет по порядку после слова формат. по счету начиная считать со слова 31 =0
# янарь это 1б март это 2 и  тд
print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Aug: {1}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28, 30, 31))