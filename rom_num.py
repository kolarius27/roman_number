# function that converts numbers to Roman numerals
# attributes: 'num' = input numeric value, 'rom' = result (Roman numeral)
def converter_num_to_rom(num, rom):
    # new variable: 'new_num' = residue of input value
    new_num = 0
    # if 'num' equals 0, goes to else and prints out the result
    if num > 0:
        # finds correct interval and adds corresponding Roman numeral to 'rom' + new residue
        if num < 4:
            rom += "I"
            new_num = num-1
        elif num == 4:
            rom += "IV"
            new_num = num-4
        elif 5 <= num < 9:
            rom += "V"
            new_num = num-5
        elif num == 9:
            rom += "IX"
            new_num = num-9
        elif 10 <= num < 40:
            rom += "X"
            new_num = num-10
        elif 40 <= num < 50:
            rom += "XL"
            new_num = num-40
        elif 50 <= num < 90:
            rom += "L"
            new_num = num-50
        elif 90 <= num < 100:
            rom += "XC"
            new_num = num-90
        elif 100 <= num < 400:
            rom += "C"
            new_num = num-100
        elif 400 <= num < 500:
            rom += "CD"
            new_num = num-400
        elif 500 <= num < 900:
            rom += "D"
            new_num = num-500
        elif 900 <= num < 1000:
            rom += "CM"
            new_num = num-900
        elif 1000 <= num:
            rom += "M"
            new_num = num-1000
        # recursion, attributes: residue of input value and to-be result
        converter_num_to_rom(new_num, rom)
    else:
        print("Result: ", rom)


# function that converts Roman numerals to numbers
# attributes: 'rom' = input Roman numeral, 'num' = result (number), 'gain' = value added to result in previous recursion
def converter_rom_to_num(rom, num, gain):
    # if length of 'rom' equals 0, goes to else and prints out the result
    # otherwise goes to corresponding if
    if len(rom) > 1:
        # new variable: 'new_gain' = value added to result in this loop
        new_gain = 0
        # looks at [-1] (or [-2] position, if needed) and adds new value to 'new_gain'
        # if two characters are needed, pops the last character of 'rom' string
        if rom[-1] == "M":
            if rom[-2] == "C":
                new_gain = 900
                num += new_gain
                rom = rom[0:len(rom)-1]
            else:
                new_gain = 1000
                num += new_gain
        elif rom[-1] == "D":
            if rom[-2] == "C":
                new_gain = 400
                num += new_gain
                rom = rom[0:len(rom)-1]
            # can't be two 'D's in Roman numeral
            elif rom[-2] == "D":
                print("Not a Roman number. Try again!")
                return False
            else:
                new_gain = 500
                num += new_gain
        elif rom[-1] == "C":
            if rom[-2] == "X":
                new_gain = 90
                num += new_gain
                rom = rom[0:len(rom) - 1]
            else:
                new_gain = 100
                num += new_gain
        elif rom[-1] == "L":
            if rom[-2] == "X":
                new_gain = 40
                num += new_gain
                rom = rom[0:len(rom) - 1]
            # can't be two 'L's in Roman numeral
            elif rom[-2] == "L":
                print("Not a Roman number. Try again!")
                return False
            else:
                new_gain = 50
                num += new_gain
        elif rom[-1] == "X":
            if rom[-2] == "I":
                new_gain = 9
                num += new_gain
                rom = rom[0:len(rom) - 1]
            else:
                new_gain = 10
                num += new_gain
        elif rom[-1] == "V":
            if rom[-2] == "I":
                new_gain = 4
                num += new_gain
                rom = rom[0:len(rom) - 1]
            # can't be two 'L's in Roman numeral
            elif rom[-2] == "V":
                print("Not a Roman number. Try again!")
                return False
            else:
                new_gain = 5
                num += new_gain
        elif rom[-1] == "I":
            new_gain = 1
            num += new_gain
    elif len(rom) == 1:
        if rom == "M":
            new_gain = 1000
            num += new_gain
        elif rom == "D":
            new_gain = 500
            num += new_gain
        elif rom == "C":
            new_gain = 100
            num += new_gain
        elif rom == "L":
            new_gain = 50
            num += new_gain
        elif rom == "X":
            new_gain = 10
            num += new_gain
        elif rom == "V":
            new_gain = 5
            num += new_gain
        elif rom == "I":
            new_gain = 1
            num += new_gain
    else:
        print("Result:", num)
        return False
    # new gain has to be bigger than gain from previous recursion
    if new_gain < gain:
        print("Not a Roman number. Try again!")
        return False
    # if ok, pops last character from 'rom' string
    # and goes through recursion
    else:
        new_rom = rom[0:len(rom)-1]
        converter_rom_to_num(new_rom, num, new_gain)


print("Hello!\n")
print("Welcome to 'Roman Numeral Converter'.")
print("With this tool you can convert numbers to Roman numerals and vice versa.")
print("If you are short of numbers to convert, just type '0'. Have fun!\n")


while True:
    # tries if input values is integer
    try:
        input_value = input("Input number: ")
        input_number = int(input_value)
        # if input_number equals 0, script stops
        if input_number == 0:
            print("Thank you for using 'Roman Numeral Converter'. Bye!")
            break
        # if input is integer, script uses function for converting numbers to Roman numerals
        converter_num_to_rom(input_number, "")
    except ValueError:
        # new variable: 'control' = if there is character not representing Roman numeral, adds 1
        control = 0
        # checks every character in input string
        # if character is not Roman numeral, adds 1 to 'control' and prints out warning
        for i in range(len(input_value)):
            if input_value[i] not in ("I", "V", "X", "L", "C", "D", "M"):
                print("Incorrect input.", "'", input_value[i], "'", "doesn't represent"
                      " any number in Roman numeral system")
                control += 1
        # if every character in input string represents Roman numeral, script uses
        # function for converting Roman numerals to numbers
        if control == 0:
            converter_rom_to_num(input_value, 0, 0)
        # if control > 0, calls input
        else:
            continue
