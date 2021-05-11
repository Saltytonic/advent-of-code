class IntcodeProcessor:
    __memory = []
    __inst_ptr = 0
    __running = False
    __filename = ""

    def set_instruction_file(self, filename):
        self.__filename = filename

    def __load_instruction_set(self):
        # Read from file and load into temp str array
        fo = open(self.__filename, "r")
        temp = fo.readline().strip().split(",")
        fo.close()
        # Load str list into memory as ints
        self.__memory = [int(i) for i in temp]

    def __incr_pointer(self, count):
        self.__inst_ptr += count

    def __read(self, addr, mode) -> int:
        if mode == 1:
            output = self.__memory[addr]
            return output
        else:
            output = self.__memory[self.__memory[addr]]
            return output

    def __write(self, addr, value):
        self.__memory[addr] = value

    def __add_instruction(self, modes):
        addr = self.__read(self.__inst_ptr+3,1)
        val = self.__read(self.__inst_ptr+2,modes[1])+self.__read(self.__inst_ptr+1,modes[0])
        self.__write(addr,val)
        self.__incr_pointer(4)

    def __multiply_instruction(self, modes):
        addr = self.__read(self.__inst_ptr+3,1)
        val = self.__read(self.__inst_ptr+2,modes[1])*self.__read(self.__inst_ptr+1,modes[0])
        self.__write(addr,val)
        self.__incr_pointer(4)

    def __input_instruction(self):
        addr = self.__read(self.__inst_ptr+1,1)
        val = int(input("Input an integer: "))
        self.__write(addr,val)
        self.__incr_pointer(2)

    def __output_instruction(self):
        print("Output >>",self.__read(self.__inst_ptr+1,0))
        self.__incr_pointer(2)

    def __exit_instruction(self):
        self.__running = False

    def __process_instruction(self):
        opcode = self.__read(self.__inst_ptr,1) % 100
        modes = [((self.__read(self.__inst_ptr,1) // 10**n) % 10) for n in range(2,5)]

        if opcode == 1:
            self.__add_instruction(modes)
        elif opcode == 2:
            self.__multiply_instruction(modes)
        elif opcode == 3:
            self.__input_instruction()
        elif opcode == 4:
            self.__output_instruction()
        elif opcode == 99:
            self.__exit_instruction()
        else:
            print("Unknown instruction",opcode)

    def start(self):
        self.__running = True
        self.__load_instruction_set()
        while self.__running:
            self.__process_instruction()


int_cpu = IntcodeProcessor()
int_cpu.set_instruction_file("input.txt")
int_cpu.start()
