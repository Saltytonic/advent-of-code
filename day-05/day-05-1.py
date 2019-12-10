class IntcodeProcessor:
    memory = []
    inst_pntr = 0

    def load_memory(self, filename):
        # Read from file and load into temp str array
        fo = open(filename, "r")
        temp = fo.readline().strip().split(",")
        fo.close()
        # Load str list into memory as ints
        memory = [int(i) for i in temp]

    def incr_pntr(self, count):
        inst_pntr += count

    def start(self):
        
while i < len(instr_list):
    # Add instruction
    if instr_list[i] == 1:
        # Get addresses for opcode
        ref_a = instr_list[i+1]
        ref_b = instr_list[i+2]
        out = instr_list[i+3]
        # Perform add operation
        instr_list[out] = instr_list[ref_a] + instr_list[ref_b]
        # Step to next instruction
        i += 4
    # Multiply instruction
    elif instr_list[i] == 2:
        # Get addresses for opcode
        ref_a = instr_list[i+1]
        ref_b = instr_list[i+2]
        out = instr_list[i+3]
        # Perform multiply operation
        instr_list[out] = instr_list[ref_a] * instr_list[ref_b]
        # Step to next instruction
        i += 4        
    # Stop execution instruction
    elif instr_list[i] == 99:
        break
    # Unknown instruction
    else:
        print("Unknown instruction")

output = open("output.txt", "w")
print(*instr_list, sep=",", file=output)
output.close()
