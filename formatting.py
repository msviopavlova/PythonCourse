for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i**2, i**3))
#                 2 is the field width after :

print()
for i in range(1, 13):
    print("No. {0:<2} squared is {1:<3} and cubed is {2:<4}".format(i, i**2, i**3))
    # now numbers are aligned to the left

print ()
for i in range(1, 13):
    print("No. {0:^2} squared is {1:^3} and cubed is {2:^4}".format(i, i**2, i**3))
    #now its aligned to the centre

print()
    #next code is about decimal places
print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:12f}".format(22/7))
print("Pi is approximately {0:12.50f}".format(22/7))
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:<72.54f}".format(22/7))
