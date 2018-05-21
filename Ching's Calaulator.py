'''
Title: Python Calculator
Author: Ching Chang
Date Created: May 16th, 2018

This is a calculator that is smart enough to keep the correct amount of
significant digits and put the answer in scientific notation if neccesary
'''

def digits(num):
    num = list(str(num))
    if "." in num:
        num.remove(".")
    while num[0] == "0":
        del num[0]
    return len(num)

def decimal(num):
    num = list(str(num))
    if "." in num:
        count = 0
        n = num.index(".") + 1
        while n < len(num):
            count += 1
            n += 1
        return count
    else:
        return 0


def sci_note(num):
    num = list(str(num))
    t = 1
    if "." in num:
        i = num.index(".")
        num.remove(".")
    else:
        i = len(num)
    while num[0] == "0":
        del num[0]
        t += 1
    num.insert(1, ".")
    n = i - t
    return str("".join(num)) + " X 10^" + str(n)

def round(num, digs):
    num = list(str(num))
    t = 1
    if "." in num:
        i = num.index(".")
        num.remove(".")
    else:
        i = len(num)
    while num[0] == "0":
        del num[0]
        t += 1
    n = i - t
    if digs < len(num):
        if int(num[digs]) > 4:
            num.insert(digs - 1, str(int(num[digs - 1]) + 1))
            del num[digs]
        num.reverse()
        while len(num) > digs:
            del num[0]
        num.reverse()
    else:
        while len(num) < digs:
            num.append("0")
    num.insert(1, ".")
    if n == 0:
        return "".join(num)
    elif n == 1:
        return str("".join(num)) + " X 10"
    else:
        return str("".join(num)) + " X 10^" + str(n)
