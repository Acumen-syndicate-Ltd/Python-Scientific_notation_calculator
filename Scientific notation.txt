# Significant digit calculator
"""
Rules
+- Round to smallest decimal place
*/ Round to smallest number of significant digits
Finding siginificant digits:
Look for the first non-zero digit from the left. Count all the digits right of that. Here are some examples:
3.00040m    has 6 sig-digs
0.0060m    has 2
0.5000055m    has 7
2018.340m    has 7
3.000 * 4.00 = 12.0
12 / 4.0 = 3.0
Rules differ for +-:
4 + 15 = 19
54 - 50 = 04 or 4
4.00501 + 5.03 = 9.04
"""

#Definitions


def length(number):
    number = list(number)
    while True:
        if "." in number:
            number.remove(".")
        elif number[0] == "0":
            number.remove(number[0])
        else:
            return len(number)

        
def decimal(number):
    number = list(number)
    decCount = 0
    if "." in number:
        while number[0]!= ".":
            number.remove(number[0])
        number.remove(number[0])
        while len(number) > 0:
            number.remove(number[0])
            decCount += 1
        return decCount
    else:
        return 0


def sci_note(number):                      #Places decimal right after first number
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



def rnd_sig(number, sig)
    number = list(str(number))


sigDig_Log = {}
dec_Log =    {}
op_Log =     {}
answer_Log = "Some sort of Error: No answer found"


#Processing


user_input = input('First number: ')

sigDig_Log[0] = length(user_input)
dec_Log[0] = decimal(user_input)

sigDig = sigDig_Log[0]
dec1 = dec_Log[0]



#Final print



if sigDig != 1 and dec1 != 1:
    print("There are " + str(sigDig) + " significant digits" +" and " + str(dec1) + " decimal places here")
elif sigDig == 1 and dec1 != 1:
    print("There is " + str(sigDig) + " significant digit" +" and " + str(dec1) + " decimal places here")
elif sigDig != 1 and dec1 == 1:
    print("There are " + str(sigDig) + " significant digits" +" and " + str(dec1) + " decimal place here")
elif sigDig == 1 and dec1 == 1:
    print("There is " + str(sigDig) + " significant digit" +" and " + str(dec1) + " decimal place here")
else:
    print("Your values are invalid. Make sure you only enter numerical inputs!")







