def converter_num_to_rom(num, rom):
    new_num = 0
    if num > 0:
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
            new_num = num - 400
        elif 500 <= num < 900:
            rom += "D"
            new_num = num-500
        elif 900 <= num < 1000:
            rom += "CM"
            new_num = num - 900
        elif 1000 <= num:
            rom += "M"
            new_num = num-1000
        converter_num_to_rom(new_num, rom)
    else:
        print("Result: ", rom)


def converter_rom_to_num(rom, num, gain):

    if len(rom) > 1:
        new_gain = 0
        if rom[-1] == "M":
            if rom[-2] == "C":
                new_gain = 900
                num += new_gain
                rom = rom[0:len(rom)-1]
            elif rom[-2] in ("D", "L", "X", "V", "I"):
                print("Not a Roman number. Try again!")
                return False
            else:
                new_gain = 1000
                num += new_gain
        elif rom[-1] == "D":
            if rom[-2] == "C":
                new_gain = 400
                num += new_gain
                rom = rom[0:len(rom)-1]
            elif rom[-2] in ("D", "L", "X", "V", "I"):
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
            elif rom[-2] in ("L", "V", "I"):
                print("Not a Roman number. Try again!")
                return False
            else:
                new_gain = 100
                num += new_gain
        elif rom[-1] == "L":
            if rom[-2] == "X":
                new_gain = 40
                num += new_gain
                rom = rom[0:len(rom) - 1]
            elif rom[-2] in ("L", "V", "I"):
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
            elif rom[-2] == "V":
                print("Not a Roman number. Try again!")
                return False
            else:
                new_gain = 10
                num += new_gain
        elif rom[-1] == "V":
            if rom[-2] == "I":
                new_gain = 4
                num += new_gain
                rom = rom[0:len(rom) - 1]
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
    if new_gain < gain:
        print("Not a Roman number. Try again!")
        return False
    else:
        new_rom = rom[0:len(rom)-1]
        converter_rom_to_num(new_rom, num, new_gain)


while True:
    try:
        input_value = input("Input number: ")
        input_number = int(input_value)
        if input_number == 0:
            print("Thank you for using 'Roman-to-Arabic/Arabic-to-Roman numeral converter'. Bye!")
            break
        converter_num_to_rom(input_number, "")
    except ValueError:
        control = 0
        for i in range(len(input_value)):
            if input_value[i] not in ("I", "V", "X", "L", "C", "D", "M"):
                print("Incorrect input.", "'", input_value[i], "'", "doesn't represent any number in Roman numeral system")
                control += 1
        if control == 0:
            converter_rom_to_num(input_value, 0, 0)
        else:
            continue
