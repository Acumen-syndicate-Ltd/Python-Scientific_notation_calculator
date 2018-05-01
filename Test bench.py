#Test bench
"""def sci_note(number):                      #Places decimal right after first number
    number = list(str(number))
    exponent = -1                         #Records the exponent for scientific notation
    num = number.copy()
    note_Log = {}
    if "." in number:
        while num[0] == "0":
            num.remove(number[0])
            number.remove(number[0])
        while number[0] != ".":
            number.remove(number[0])
            exponent += 1
        print(exponent)
        
        num.remove(".")
        num.insert(1, ".")
        num = "".join(num)
        
        return {0: num, 1: exponent}               #Currently does not return with num * 10^x
    
    else:
        number = "".join(number)
        return {0: number, 1: 0}


t = sci_note(input("Declare a number: "))
print(t)"""






#Work on this one next

def rnd_Dec(number, dec):
    dec = int(dec)
    number = list(str(number))
    org = number
    wholeList = []
    length = 0
    while True:
        if number[0] != ".":
            wholeList = wholeList.extend(number[0])
            number.remove(number[0])
        elif number[0] == ".":
            wholeList = wholeList.extend(number[0])
            number.remove(number[0])
            if int(number[dec]) >=  5:
                if int(number[dec - 1]) <= 8:
                    number.remove(number[dec-1])  int(number[dec-1]) + 1 #Start off here

t = rnd_Dec(input("Number here: "), input("Decimal places here: "))
print(t)



























"""
def rnd_sci_note(number, sig): #Creates scientific notation as well. Input only floats
    sig = int(sig) - 1
    
    note = sci_note(number)   #Finds and rounds number
    copy = note
    exp = []
    note = note.split(" * ")
    num = float(note[0])
    num = list(str(round(num, sig)))
    if "." in num:                   
        sig += 2

    copy = list(copy[::-1])    #Finds and stores exponent value
    while copy[0] != '^':
        exp.insert(0, copy[0])
        copy.remove(copy[0])
    exp = "".join(exp)
    exp_num = int(exp)

    while len(num) < sig:    #Adds zeros for proper sig digs
        num.append("0")
        
    num_str = "".join(num)     #In case of rounding up, so 10 * 10^3 == 1 * 10^4
    if "10." in num_str:
        num.remove(num[1])
        num.insert(2, "0")
        
        exp_num += 1
        copy = copy[::-1]
        copy.append(str(exp_num))
        copy = "".join(copy)
        copy = copy.split(" * ")
        
        num = "".join(num)
        copy.remove(copy[0])      
        copy.insert(0, num)
        rnd = " * ".join(copy)
        return rnd
       
    num = "".join(num)
    note.remove(note[0])      #Creates string with rounded number
    note.insert(0, num)
    rnd = " * ".join(note)

    return rnd
"""


"""def sci_note(number):                      #Places decimal right after first number
    number = list(str(number))
    exponent = -1                         #Records the exponent for scientific notation
    num = number.copy()  #Stores original list
    note_Log = {}                 
    i = 0
    if "." in number:          #For floats
        while num[0] == "0":                    #Removes all frontal zeros
            num.remove(number[0])
            number.remove(number[0])
            if num[0] == ".":          #Takes out decimal
                num.remove(number[0])
                number.remove(number[0])                 
                while num[0] == "0":     #Removes frontal zeros after decimal for negative exponents
                    if i == 1:
                        exponent = 0 #Resets exponent
                        i = 1
                    num.remove(number[0])
                    number.remove(number[0])
                    exponent -= 1 #Negative exps
                    
        while number[0] != "." and "." in number: #Find required positive exponent
            number.remove(number[0])
            exponent += 1
        if "." in num:       #Converts to scientific number
            num.remove(".")
        num.insert(1, ".")
        num = "".join(num)
        
        note_Log = {0: num, 1: exponent}#Final
    
    else:                                                 #For integral numbers
        while number[0] == "0": #Removes frontal zeros
            number.remove(number[0])
            num.remove(num[0])
        while i < len(num):                     #Finds total sig digs in list, for exponent value
            number.remove(number[0])
            i += 1                        #i records iteration count
            exponent += 1
        num.insert(1, ".")
        num = "".join(num)
        note_Log = {0: num, 1: exponent}#Final

    return str(note_Log[0]) + " * 10^" + str(note_Log[1])  #Returns in scientific notation


print(sci_note(input("Declare a number: ")))"""

"""
def sci_note(number):
    number = list(str(number))                #Places decimal right after first number
    if "." in number:
        
        exponent = -1                    #Records the exponent for scientific notation
        num = number.copy()
        while num[0] == "0":
            num.remove(number[0])
        num = "".join(num)
        return num





t = sci_note(000000500.05)


print(t)"""


"""
------------------------------------------------------------------------------------------------------------------
var1 = input("Type a number here: ")

var1 = list(var1)
var2 = var1.copy()              #Variable linking happenes when simple data is assigned complex data
var1.remove(var1[0])

print(var2)
print("This is var1" + str(var1))
------------------------------------------------------------------------------------------------------------------
"""




























"""def f(x):
    num = 550
    var = num
    num = str(num)
    print(var)
    if num == 550:
        print("False")
    else:
        print("True")
    num = list(num)
    print(var)
    num.insert(1, 0)
    print(var)
    print(num)
    print(var + " and another one 3")

f(3)
"""
