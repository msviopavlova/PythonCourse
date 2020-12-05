for hello in range(1, 21):
    if hello%3==0 or  hello%5==0:
        continue #makes the line skip the thing that matches the condition, not execute it!!!
    print(hello)

