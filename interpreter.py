import argparse

def word(input):
    "Converts a MIPS 'word' command into binary machine code (as a string)."
    if len(input)!= 1:
        return "".join(map(str, input))
    
    return bin(int(input[0]))[2:].zfill(32)

def add(input):
    "Converts a MIPS 'add' command into binary machine code (as a string)."
    if len(input)!= 3:
        return "".join(map(str, input))
    
    return "000000" + bin(int(input[1][1:-1]))[2:].zfill(5) + bin(int(input[2][1:]))[2:].zfill(5) + bin(int(input[0][1:-1]))[2:].zfill(5) + "00000100000"

def sub(input):
    "Converts a MIPS 'sub' command into binary machine code (as a string)."
    if len(input)!= 3:
        return "".join(map(str, input))
    
    return "000000" + bin(int(input[1][1:-1]))[2:].zfill(5) + bin(int(input[2][1:]))[2:].zfill(5) + bin(int(input[0][1:-1]))[2:].zfill(5) + "00000100010"

def mult(input):
    "Converts a MIPS 'mult' command into binary machine code (as a string)."
    if len(input)!= 2:
        return "".join(map(str, input))
    
    return "000000" + bin(int(input[0][1:-1]))[2:].zfill(5) + bin(int(input[1][1:]))[2:].zfill(5) + "00000" + "00000011000"

def multu(input):
    "Converts a MIPS 'multu' command into binary machine code (as a string)."
    if len(input)!= 2:
        return "".join(map(str, input))
    
    return "000000" + bin(int(input[0][1:-1]))[2:].zfill(5) + bin(int(input[1][1:]))[2:].zfill(5) + "00000" + "00000011001"

def div(input):
    "Converts a MIPS 'div' command into binary machine code (as a string)."
    if len(input)!= 2:
        return "".join(map(str, input))
    
    return "000000" + bin(int(input[0][1:-1]))[2:].zfill(5) + bin(int(input[1][1:]))[2:].zfill(5) + "00000" + "00000011010"

def divu(input):
    "Converts a MIPS 'divu' command into binary machine code (as a string)."
    if len(input)!= 2:
        return "".join(map(str, input))
    
    return "000000" + bin(int(input[0][1:-1]))[2:].zfill(5) + bin(int(input[1][1:]))[2:].zfill(5) + "00000" + "00000011011"

def mfhi(input):
    "Converts a MIPS 'mfhi' command into binary machine code (as a string)."
    if len(input)!= 1:
        return "".join(map(str, input))

    return '0' * 16 + bin(int(input[0][1:]))[2:].zfill(5) + "00000010000"

def mflo(input):
    "Converts a MIPS 'mflo' command into binary machine code (as a string)."
    if len(input)!= 1:
        return "".join(map(str, input))

    return '0' * 16 + bin(int(input[0][1:]))[2:].zfill(5) + "00000010010"

def lis(input):
    "Converts a MIPS 'lis' command into binary machine code (as a string)."
    if len(input)!= 1:
        return "".join(map(str, input))

    return '0' * 16 + bin(int(input[0][1:]))[2:].zfill(5) + "00000010100"

def beq(input):
    "Converts a MIPS 'beq' command into binary machine code (as a string)."
    if len(input)!= 3:
        return "".join(map(str, input))

    return "000100" + bin(int(input[0][1:-1]))[2:].zfill(5) + bin(int(input[1][1:-1]))[2:].zfill(5) + bin(int(input[2]))[2:].zfill(16)

def bne(input):
    "Converts a MIPS 'bne' command into binary machine code (as a string)."
    if len(input)!= 3:
        return "".join(map(str, input))

    return "000101" + bin(int(input[0][1:-1]))[2:].zfill(5) + bin(int(input[1][1:-1]))[2:].zfill(5) + bin(int(input[2]))[2:].zfill(16)

def jr(input):
    "Converts a MIPS 'jr' command into binary machine code (as a string)."
    if len(input)!= 1:
        return "".join(map(str, input))

    return '0' * 6 + bin(int(input[0][1:]))[2:].zfill(5) + '0' * 17 + "1000"

def process(input):
    """
    Processes a line of MIPS code and converts it to binary machine code
    (as a string).
    """

    command = input[0].lower()

    if command == "add": return add(input[1:])
    elif command == "sub": return sub(input[1:])
    elif command == "mult": return mult(input[1:])
    elif command == "multu": return multu(input[1:])
    elif command == "div": return div(input[1:])
    elif command == "divu": return divu(input[1:])
    elif command == "mfhi": return mfhi(input[1:])
    elif command == "mflo": return mflo(input[1:])
    elif command == "lis": return lis(input[1:])
    elif command == "beq": return beq(input[1:])
    elif command == "bne": return bne(input[1:])
    elif command == "jr": return jr(input[1:])
    else: raise Exception("Invalid MIPS command.  " + command)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--line', type=str, help="input a line of MIPS code.")
    parser.add_argument('--in_file', type=str, help="txt file containing MIPS instructions")
    parser.add_argument('--out_file', type=str, help='output to a file instead of std')
    args = parser.parse_args()

    result = []
    if args.line:
        input = args.line.split(' ')
        result.append('.word 0x' + str(hex(int(process(input), 2)))[2:].zfill(8))

    if args.in_file:
        f_in = open(args.in_file, 'r')
        for line in f_in:
            input = line.split(' ')
            result.append('.word 0x' + str(hex(int(process(input), 2)))[2:].zfill(8))

    if args.out_file:
        f = open(args.out_file, 'w+')
        for row in result:
            f.write(row + '\n')
    else:
        for row in result:
            print(row)