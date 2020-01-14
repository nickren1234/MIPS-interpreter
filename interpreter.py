import argparse

class Parser:
    def __init__(self):
        self.result = []


    def word(self, input):
        "Converts a MIPS 'word' command into binary machine code (as a string)."
        if len(input)!= 1:
            self.result.append("".join(map(str, input)))
        
        return bin(int(input[0]))[2:].zfill(32)

    def add(self, input):
        "Converts a MIPS 'add' command into binary machine code (as a string)."
        if len(input)!= 3:
            self.result.append("".join(map(str, input)))
        
        self.result.append("000000" + bin(int(input[1][1:-1]))[2:].zfill(5) + bin(int(input[2][1:]))[2:].zfill(5) + bin(int(input[0][1:-1]))[2:].zfill(5) + "00000100000")

    def sub(self, input):
        "Converts a MIPS 'sub' command into binary machine code (as a string)."
        if len(input)!= 3:
            self.result.append("".join(map(str, input)))
        
        self.result.append("000000" + bin(int(input[1][1:-1]))[2:].zfill(5) + bin(int(input[2][1:]))[2:].zfill(5) + bin(int(input[0][1:-1]))[2:].zfill(5) + "00000100010")

    def mult(self, input):
        "Converts a MIPS 'mult' command into binary machine code (as a string)."
        if len(input)!= 2:
            self.result.append("".join(map(str, input)))
        
        self.result.append("000000" + bin(int(input[0][1:-1]))[2:].zfill(5) + bin(int(input[1][1:]))[2:].zfill(5) + "00000" + "00000011000")

    def multu(self, input):
        "Converts a MIPS 'multu' command into binary machine code (as a string)."
        if len(input)!= 2:
            self.result.append("".join(map(str, input)))
        
        self.result.append("000000" + bin(int(input[0][1:-1]))[2:].zfill(5) + bin(int(input[1][1:]))[2:].zfill(5) + "00000" + "00000011001")

    def div(self, input):
        "Converts a MIPS 'div' command into binary machine code (as a string)."
        if len(input)!= 2:
            self.result.append("".join(map(str, input)))
        
        self.result.append("000000" + bin(int(input[0][1:-1]))[2:].zfill(5) + bin(int(input[1][1:]))[2:].zfill(5) + "00000" + "00000011010")

    def divu(self, input):
        "Converts a MIPS 'divu' command into binary machine code (as a string)."
        if len(input)!= 2:
            self.result.append("".join(map(str, input)))
        
        self.result.append("000000" + bin(int(input[0][1:-1]))[2:].zfill(5) + bin(int(input[1][1:]))[2:].zfill(5) + "00000" + "00000011011")

    def mfhi(self, input):
        "Converts a MIPS 'mfhi' command into binary machine code (as a string)."
        if len(input)!= 1:
            self.result.append("".join(map(str, input)))

        self.result.append('0' * 16 + bin(int(input[0][1:]))[2:].zfill(5) + "00000010000")

    def mflo(self, input):
        "Converts a MIPS 'mflo' command into binary machine code (as a string)."
        if len(input)!= 1:
            self.result.append("".join(map(str, input)))

        self.result.append('0' * 16 + bin(int(input[0][1:]))[2:].zfill(5) + "00000010010")

    def lis(self, input):
        "Converts a MIPS 'lis' command into binary machine code (as a string)."
        if len(input)!= 1:
            self.result.append("".join(map(str, input)))

        self.result.append('0' * 16 + bin(int(input[0][1:]))[2:].zfill(5) + "00000010100")

    def beq(self, input):
        "Converts a MIPS 'beq' command into binary machine code (as a string)."
        if len(input)!= 3:
            self.result.append("".join(map(str, input)))

        self.result.append("000100" + bin(int(input[0][1:-1]))[2:].zfill(5) + bin(int(input[1][1:-1]))[2:].zfill(5) + bin(int(input[2]))[2:].zfill(16))

    def bne(self, input):
        "Converts a MIPS 'bne' command into binary machine code (as a string)."
        if len(input)!= 3:
            self.result.append("".join(map(str, input)))

        self.result.append("000101" + bin(int(input[0][1:-1]))[2:].zfill(5) + bin(int(input[1][1:-1]))[2:].zfill(5) + bin(int(input[2]))[2:].zfill(16))

    def jr(self, input):
        "Converts a MIPS 'jr' command into binary machine code (as a string)."
        if len(input)!= 1:
            self.result.append("".join(map(str, input)))

        self.result.append('0' * 6 + bin(int(input[0][1:]))[2:].zfill(5) + '0' * 17 + "1000")

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--line', type=str, help="input a line of MIPS code.")
    arg_parser.add_argument('--in_file', type=str, help="txt file containing MIPS instructions")
    arg_parser.add_argument('--out_file', type=str, help='output to a file instead of std')
    args = arg_parser.parse_args()

    parser = Parser()
    if args.line:
        input = args.line.split(' ')
        if input[0] = '.word':
            input[0] = input[0][1:]
        func = getattr(parser, input[0].lower())
        func(input[1:])

    if args.in_file:
        f_in = open(args.in_file, 'r')
        for line in f_in:
            input = line.split(' ')
            if input[0] = '.word':
                input[0] = input[0][1:]
            func = getattr(parser, input[0].lower())
            func(input[1:])

    if args.out_file:
        f = open(args.out_file, 'w+')
        for row in parser.result:
            f.write('.word 0x' + str(hex(int(row, 2)))[2:].zfill(8) + '\n')
    else:
        for row in parser.result:
            print('.word 0x' + str(hex(int(row, 2)))[2:].zfill(8))