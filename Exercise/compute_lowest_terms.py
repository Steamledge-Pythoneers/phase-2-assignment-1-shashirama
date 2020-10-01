## TODO: complete the function "lowest_terms" below
# HCF finder function
def Hcf(num1, num2):
    if num1 and num2 < 0:
        smaller = abs(num1)
    elif num1 < 0:
        smaller = num2
    elif num2 < 0:
        smaller = num1
    elif num1 > num2:
        smaller = num2
    else:
        smaller = num1

    for s in range(1, smaller + 1):
        if (num1 % s == 0) and (num2 % s == 0):
            hcf = s
    return hcf

def lowest_terms(x):
    # splitting x with x1 as numerator and x2 as denominator
    x_split = x.split("/")
    x1, x2 = map(int, x_split)
    if x1 == 0:
        return "0"
    elif x2 == 0:
        return "Undefined"
    else:
        hcf = Hcf(x1, x2)
        numerator = x1 // hcf
        denominator = x2 // hcf
        if denominator < 0:
            numerator*=-1
            solution2 = "{}/{}".format((numerator), abs(denominator))
            return solution2
        elif numerator and denominator < 0:
            solution = "{}/{}".format(abs(numerator), abs(denominator))
            return solution

        else:
            solution1 = "{}/{}".format(numerator, denominator)
            return solution1

#print(Hcf(0, 0))





