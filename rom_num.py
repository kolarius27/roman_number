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

def converter_rom_to_num(rom, num):
    if len(rom) == 1:
        if rom == "M":
            num += 1000
        elif rom == "D":
            num += 500
        elif rom == "C":
            num += 100
        elif rom == "L":
            num += 50
        elif rom == "X":
            num += 10
        elif rom == "V":
            num += 5
        elif rom == "I":
            num += 1
        print("Result:", num)
    elif len(rom) > 1:
        if rom[0] == "M":
            num += 1000
        elif rom[0] == "D":
            if rom[1] is in ("M", "D"):
                print("Not a Roman number. Try again!")
                return False
            else:
                num += 500
        elif rom[0] == "C":
            if rom[1] == "M":
                num += 900
                rom = rom[1:len(rom)]
            elif rom[1] == "D":
                num += 400
                rom = rom[1:len(rom)]
            else:
                num += 100
        elif rom[0] == "L":
            if rom[1] in ("M", "D", "C"):
                print("Not a Roman number. Try again!")
                return False
            else:
                num += 50
        elif rom[0] == "X":
            if rom[1] == "C":
                num += 90
                rom = rom[1:len(rom)]
            elif rom[1] == "L":
                num += 40
                rom = rom[1:len(rom)]
            elif rom[1] in ("M", "D"):
                print("Not a Roman number. Try again!")
                return False
            else:
                num += 10
        elif rom[0] == "V":
            if rom[1] in ("M", "D", "C", "L", "X"):
                print("Not a Roman number. Try again!")
                return False
            else:
                num += 5
        elif rom[0] == "I":
            if rom[1] == "X":
                num += 9
                rom = rom[1:len(rom)]
            elif rom[1] == "V":
                num += 4
                rom = rom[1:len(rom)]
            elif rom[1] in ("M", "D", "C", "L"):
                print("Not a Roman number. Try again!")
                return False
            else:
                num += 1
        new_rom = rom[1:len(rom)]
        converter_rom_to_num(new_rom, num)
    else:
        print("Result:", num)


def converter_rom_to_num(rom, num):
    if rom[-1] == "M":
        if rom[-2] == "C":
            num += 900
            rom = rom[0:len(rom)-1]
        if rom[-2] is in ("D", "L", "X", "V", "I"):
            print("Not a Roman number. Try again!")
            return False
        else:
            num += 1000
    if rom[-1] == "D":
        if rom[-2] == "C":



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
            converter_rom_to_num(input_value, 0)
        else:
            continue
