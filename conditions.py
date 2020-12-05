age = int(input("How old are you? "))

#if age >=16 and age<65:   and stops working once it finds the first condition that is false
#if 16<= age <=65:
if age in range(1, 66):
    print("Have a good dau at work")
else:
    print("Enjoy your free time")

print("-"*80)

if age<16 or age>65:   #or stops working once it finds the first condition that is true
    print("Enjoy your free time")
else:
    print("Have a good day at  work")


