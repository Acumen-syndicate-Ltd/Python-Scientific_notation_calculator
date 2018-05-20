'''
Title: Python Calculator
Author: Ching Chang
Date Created: May 16th, 2018

This is a calculator that is smart enough to keep the correct amount of sig-digs and put the
answer in scientific notation if neccesary
'''

def listify(num):
    num = str(num)
    number = []
    n = 0
    for i in num:
        number.append(num[n])
        n += 1
    return (number)

def digits(num):
    number = listify(num)
    if "." in number:
        number.remove(".")
    while number[0] == "0":
        number.remove("0")
    return len(number)

def decimal(num):
    number = listify(num)
    if "." in number:
        count = 0
        n = number.index(".") + 1
        while n < len(number):
            count += 1
            n += 1
        return count
    else:
        return 0

def sci_note(num):
    number = listify(num)
    if "." in number:
        i = number.index(".")
        number.remove(".")
    else:
        i = len(number)
    while number[0] == "0":
        number.remove[0]
    number.insert(1, ".")
    n = i - 1
    return str("".join(number)) + " X 10^ " + str(n)
