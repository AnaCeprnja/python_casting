def find_lcm(x, y):

    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm


num1 = 30
num2 = 50

print("The L.C.M. is", find_lcm(num1, num2))
