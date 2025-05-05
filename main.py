def bin_to_dec(bin_number):  # this function will take binary number from the user and convert it to decimal number
    sum = 0
    power = 0
    diget = 0
    binary_number = int(bin_number)
    while binary_number > 0:
        diget = binary_number % 10
        sum = sum + diget * (2 ** power)
        binary_number = binary_number // 10
        power = power + 1
    return (sum)


########################
def bin_to_octal(binary_number):  # this function will take binary number from the user and convert it to octaal number
    ls_diget = 0
    three_diget = 0
    power = 0
    sum = 0
    answer = ""
    while binary_number > 0:
        three_diget = binary_number % 1000
        sum = 0
        power = 0
        while three_diget > 0:
            ls_diget = three_diget % 10
            sum = sum + ls_diget * (2 ** power)
            three_diget = three_diget // 10
            power = power + 1
        answer = str(sum) + answer
        binary_number = binary_number // 1000
    return answer


#########################################
def bin_to_hexa(
        binary_number):  # this function will take binary number from the user and convert it to hexadecimal number
    ls_diget = 0
    three_diget = 0
    power = 0
    sum = 0
    answer = ""
    while binary_number > 0:
        four_diget = binary_number % 10000
        sum = 0
        power = 0
        while four_diget > 0:
            ls_diget = four_diget % 10
            sum = sum + ls_diget * (2 ** power)
            four_diget = four_diget // 10
            power = power + 1
        if sum == 10:
            sum = "A"
        elif sum == 11:
            sum = "B"
        elif sum == 12:
            sum = "C"
        elif sum == 13:
            sum = "D"
        elif sum == 14:
            sum = "E"
        elif sum == 15:
            sum = "F"
        answer = str(sum) + answer
        binary_number = binary_number // 10000
    return answer


#######################################
def hexa_to_bin(
        hexa16_number):  # this function will take hexa decimal  number from the user and convert it to binary number
    hex_number = 0
    result = 0
    reminder = 0
    answer = ""
    for i in range(len(str(hexa16_number)) - 1, -1, -1):
        if hexa16_number[i] == "A" or hexa16_number[i] == "a":
            hex_number = 10
        elif hexa16_number[i] == "B" or hexa16_number[i] == "b":
            hex_number = 11
        elif hexa16_number[i] == "C" or hexa16_number[i] == "c":
            hex_number = 12
        elif hexa16_number[i] == "D" or hexa16_number[i] == "d":
            hex_number = 13
        elif hexa16_number[i] == "E" or hexa16_number[i] == "e":
            hex_number = 14
        elif hexa16_number[i] == "F" or hexa16_number[i] == "f":
            hex_number = 15
        else:
            hex_number = int(hexa16_number[i])
        for j in range(0, 4):
            reminder = hex_number % 2
            hex_number = hex_number // 2
            answer = str(reminder) + answer
    return answer


################################################
def oct_to_bin(oct8_number):  # this function will take Ctal number from the user and convert it to binary number
    oct_number = 0
    result = 0
    reminder = 0
    answer = ""
    for i in range(len(str(oct8_number)) - 1, -1, -1):
        oct_number = int(oct8_number[i])
        for j in range(0, 3):
            reminder = oct_number % 2
            oct_number = oct_number // 2
            answer = str(reminder) + answer
    return answer


#######################################
def decimal_to_hexadecimal(num):
    hexadecimal_num = ""
    while num > 0:
        remainder = num % 16
        if remainder < 10:
            hexadecimal_num = str(remainder) + hexadecimal_num
        else:
            hexadecimal_num = chr(65 + remainder - 10) + hexadecimal_num
        num = num // 16
    return hexadecimal_num


#########################################

def hexadecimal_to_decimal(hex_num):
    decimal_num = 0
    hex_digits = "0123456789ABCDEF"

    for digit in hex_num:
        decimal_num = decimal_num * 16 + hex_digits.index(digit.upper())

    return decimal_num


####################################
def decimal_to_bin(n):
    s = ""
    while (n > 0):
        bin = n % 2
        s = str(bin) + s
        n = n // 2
        return (int(s))


###################################
def decimal_to_octal(num):
    octal_num = ""
    while num > 0:
        remainder = num % 8
        octal_num = str(remainder) + octal_num
        num = num // 8
    return octal_num


##########################
def hex_to_oct():
    hex_num = input("Enter your hexadecimal number: ")
    dec_val = int(hex_num, 16)
    oct_val = ""

    while dec_val > 0:
        digit = dec_val % 8
        oct_val = str(digit) + oct_val
        dec_val = dec_val // 8
    return (oct_val)


#################################3
def oct_to_dec(num):
    num = int(input("Enter your octal number: "))
    dec = 0
    i = 0
    while num > 0:
        digit = num % 10
        dec = dec + digit * (8 ** i)
        num = num // 10
        i = i + 1
    return (dec)


##################################
def oct_to_hex():
    num = int(input("Enter your octal number: "))
    hex_val = ""
    dec = 0
    i = 0

    while num > 0:
        digit = num % 10
        dec = dec + digit * (8 ** i)
        num = num // 10
        i = i + 1

    while dec > 0:
        remainder = dec % 16
        if remainder < 10:
            hex_val = str(remainder) + hex_val
        else:
            hex_val = chr(ord('A') + remainder - 10) + hex_val
        dec = dec // 16

    return (hex_val)


##############################
def is_binary_number(binary_str):
    for digit in binary_str:
        if digit not in '01':
            return False
        else:
            return True
        ###############################


def is_octal_number(octal_str):
    try:
        int_value = int(octal_str, 8)
        return oct(int_value) == octal_str
    except ValueError:
        return False


#########################
def is_hexadecimal_number(hex_str):
    try:
        int_value = int(hex_str, 16)
        return hex(int_value) == hex_str
    except ValueError:
        return False


###########################
def is_decimal_number(decimal_str):
    try:
        float_value = float(decimal_str)
        return True
    except ValueError:
        return False


###################################

def checkbinNumber(num):
    pass


def checkoctnumber(num):
    pass


while (True):
    print("** numbering system converter **", "A)insert a new number", "B)Exit program", sep='\n')
    x = input()
    if (x == 'A'):
        bool1 = True
        num = input("Please insert a number: ")
        while (bool1 == True):

            print("** Please select the base you want to convert a number from**", "A)Decimal", "B)Binary", "C)Octal",
                  "D)hexadecimal", sep='\n')
            choice = input()
            if (choice == 'A'):
                base = 10
            elif (choice == 'B'):
                if (is_binary_number(num)):
                    base = 2
                else:
                    break
            elif (choice == 'C'):
                if (checkoctnumber(num)):
                    base = 8
                else:
                    break
            elif (choice == 'D'):
                base = 16
            else:
                print("please select a valid choice")
                continue
            if (choice == 'A' or choice == 'B' or choice == 'C' or choice == 'D'):
                bool2 = True
                while (bool2 == True):
                    print("** Please select the base you want to convert a number to **", "A)Decimal", "B)Binary",
                          "C)Octal", "D)hexadecimal", sep='\n')
                    bases = input()
                    flag3 = True
                    while (flag3 == True):
                        if (bases == 'A'):
                            base2 = 10
                        elif (bases == 'B'):
                            if (checkbinNumber(num)):
                                base = 2
                            else:
                                break
                        elif (bases == 'C'):
                            if (checkoctnumber(num)):
                                base = 8
                            else:
                                break
                        elif (bases == 'D'):
                            base2 = 16
                        else:
                            print("please select a valid choice")

                            break;
                        if (base == 10):
                            if (base2 == 10):
                                print(num)
                                bool1 = False
                                bool2 = False
                                break
                            elif (base2 == 2):
                                print(decimal_to_bin(num))
                                bool1 = False
                                bool2 = False
                                break
                            elif (base2 == 8):
                                print(decimal_to_octal(num))
                                bool1 = False
                                bool2 = False
                                break
                            elif (base2 == 16):
                                print(decimal_to_hexadecimal(num))
                                bool1 = False
                                bool2 = False
                                break
                        elif (base == 2):
                            if (base2 == 2):
                                print(num)
                                bool1 = False
                                bool2 = False
                                break
                            elif (base2 == 10):
                                print(bin_to_dec(num))
                                bool1 = False
                                bool2 = False
                                break
                            elif (base2 == 8):
                                print(bin_to_octal(num))
                                bool1 = False
                                bool2 = False
                                break
                            elif (base2 == 16):
                                print(bin_to_hexa(num))
                                bool1 = False
                                bool2 = False
                                break
                        elif (base == 8):
                            if (base2 == 8):
                                print(num)
                                bool1 = False
                                bool2 = False
                                break
                            elif (base2 == 2):
                                print(oct_to_bin(num))
                                bool1 = False
                                bool2 = False
                                break
                            elif (base2 == 10):
                                print(oct_to_dec(num))
                                bool1 = False
                                bool2 = False
                                break
                            elif (base2 == 16):
                                print(oct_to_hex(num))
                                bool1 = False
                                bool2 = False
                                break
                        elif (base == 16):
                            if (base2 == 16):
                                print(num)
                                bool1 = False
                                bool2 = False
                                break
                            elif (base2 == 2):
                                print(hexa_to_bin(num))
                                bool1 = False
                                bool2 = False
                                break;
                            elif (base2 == 8):
                                print(hex_to_oct(num))
                                bool1 = False
                                bool2 = False
                                break
                            elif (base2 == 10):
                                print(hexadecimal_to_decimal(num))
                                bool1 = False
                                bool2 = False
                                break
    elif (x == 'B'):
        break
    else:
        print("please select a valid choice")